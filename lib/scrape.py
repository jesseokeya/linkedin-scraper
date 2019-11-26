from os import remove
from typing import List
from json import dump, load
from time import sleep, time
from selenium import webdriver
from os.path import abspath, dirname, exists

from .helper import Helper


class Scrape(Helper):
    def __init__(self, url: str = ''):
        super().__init__(url)
        self.base_dir = dirname(dirname(abspath(__file__)))
        self.chrome_exec = f'{self.base_dir}/chromedriver'
        self.chrome_driver = webdriver.Chrome(executable_path=self.chrome_exec)
        self.chrome_driver.get(url)
        self.chrome_driver.implicitly_wait(5)
        self.url = url

    def login(self, **kwargs) -> None:
        try:
            driver: WebDriver = self.chrome_driver

            username: str = kwargs['username']
            password: str = kwargs['password']

            login_xpath: str = "//a[@data-tracking-control-name='guest_homepage-basic_nav-header-signin']"
            login_button_xpath: str = "//button[@aria-label='Sign in']"

            driver.find_element_by_xpath(login_xpath).click()

            username_input: None = driver.find_element_by_id('username')
            password_input: None = driver.find_element_by_id('password')

            username_input.send_keys(username)
            password_input.send_keys(password)

            driver.find_element_by_xpath(login_button_xpath).click()

        except Exception as e:
            self.handle_error(e, 'Error occured during login')

    def retrieve_images(self) -> List[str]:
        try:
            results: list = []

            driver: WebDriver = self.chrome_driver
            images: None = driver.find_elements_by_tag_name('img')

            for image in images:
                source: str = image.get_attribute('src')
                if source != None and source.find('data:image/') == -1:
                    results.append(source)

            return results
        except Exception as e:
            self.handle_error(e, 'Error occured while retrieving images')

    def retrieve_videos(self) -> List[str]:
        try:
            results: list = []

            driver: WebDriver = self.chrome_driver
            videos: None = driver.find_elements_by_tag_name('video')

            for video in videos:
                source: str = video.get_attribute('src')
                if source != None and source.find('ads.linkedin.com') == -1:
                    results.append(source)

            return results
        except Exception as e:
            self.handle_error(e, 'Error occured while retrieving videos')

    def scroll_to_bottom(self, scroll_time_limit: int = 5) -> None:
        try:
            driver: WebDriver = self.chrome_driver

            SCROLL_PAUSE_TIME: int = 0.5

            # Get scroll height
            last_height = driver.execute_script(
                "return document.body.scrollHeight")
            old_time: float = time()
            loop_control: bool = True

            while loop_control:
                current_time: float = time()
                # Scroll down to bottom
                driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);")

                # Wait to load page
                self.__duration(SCROLL_PAUSE_TIME)

                # Calculate new scroll height and compare with last scroll height
                new_height: None = driver.execute_script(
                    "return document.body.scrollHeight")
                scroll_time_passed: float = (
                    current_time - old_time) > scroll_time_limit

                if (new_height == last_height) or scroll_time_passed:
                    loop_control: bool = False

                last_height = new_height

        except Exception as e:
            self.handle_error(
                e, 'Error occured while scrolling page to bottom')

    def write_file(self, *args) -> None:
        try:
            file_data: set = args[0]
            file_name: str = args[1]

            file_path: str = f'{self.base_dir}/{file_name}'
            path_exists = exists(file_path)

            file_ctx = open(
                file_path, 'r+') if path_exists else open(file_path, 'w+')

            if not path_exists:
                dump(file_data, file_ctx, indent=4)
            else:
                remove(file_path)
                self.write_file(file_data, file_name)

        except Exception as e:
            self.handle_error(e, 'Error occured while writing to file')

    def get_url(self) -> str:
        try:
            return self.url
        except Exception as e:
            print(e, 'Error occured during login')

    def end(self, seconds: int) -> None:
        try:
            self.__duration(seconds)
            return self.chrome_driver.quit()
        except Exception as e:
            self.handle_error(
                e, 'Error occured while closing the chrome driver')

    def __duration(self, seconds: int = 0) -> None:
        try:
            return sleep(seconds)
        except Exception as e:
            self.handle_error(e, 'Error occured in chrome driver duration')
