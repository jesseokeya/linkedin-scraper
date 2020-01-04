from lib import Scrape
from typing import List


def main():
    seconds: int = 60
    username: str = 'jesseokeya@gmail.com'
    password: str = 'Chukwudifu1'

    # Navigates to Linkedin's website
    scrapper = Scrape()

    # Takes in credentials to login into the url sepecified
    scrapper.login(username=username, password=password)

    # Navigate to specified pages on the website
    scrapper.navigate_to('profile', duration=2)
    scrapper.navigate_to(
        multiple=['notifications', 'messages', 'network', 'jobs' 'home'],
        duration=2
    )

    # Scroll to the bottom of page for 10 seconds
    # The longer you scroll the more data you collect from linkedin
    scrapper.scroll_to_bottom(10)

    # Returns a list of all images on website
    images: List[str] = scrapper.retrieve_images()

    # Returns a list of all videos on website
    videos: List[str] = scrapper.retrieve_videos()

    # Build data scrapped into a set
    file_data: set = {
        'images': images,
        'videos': videos
    }

    # create and write file data to json file
    scrapper.write_file(file_data, 'data.json')

    # Uncomment to end the selenium chrome driver after 60 seconds
    # scrapper.end(seconds)


main()
