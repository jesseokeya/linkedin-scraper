from lib import Scrape
from typing import List
from os import environ

def main():
    seconds: int = 60
    username: str = environ.get('EMAIL')
    password: str = environ.get('PASSWORD')

    # Navigates to Linkedin's website
    scraper = Scrape()

    # Takes in credentials to login into the url sepecified
    scraper.login(username=username, password=password)

    # Navigate to specified pages on the website
    scraper.navigate_to('profile', duration=2)
    scraper.navigate_to(
        multiple=['notifications', 'messages', 'network', 'jobs', 'home'],
        duration=2
    )

    # Scroll to the bottom of page for 10 seconds
    # The longer you scroll the more data you collect from linkedin
    scraper.scroll_to_bottom(10)

    # Returns a list of all images on website
    images: List[str] = scraper.retrieve_images()

    # Returns a list of all videos on website
    videos: List[str] = scraper.retrieve_videos()

    # Build data scrapped into a set
    file_data: set = {
        'images': images,
        'videos': videos
    }

    # print scrapped information before saving to file
    print(file_data)

    # create and write file data to json file
    scraper.write_file(file_data, 'data.json')

    # Uncomment to end the selenium chrome driver after 60 seconds
    # scraper.end(seconds)

main()
