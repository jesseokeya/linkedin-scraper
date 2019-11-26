from lib import Scrape
from typing import List

def main():
    url: str = 'https://www.linkedin.com/'
    seconds: int = 60
    username: str = 'jesseokeya@gmail.com'
    password: str = 'Chukwudifu1'

    # Navigates to the url specified
    scrapper = Scrape(url)
    return
    # Takes in credentials to login into the url sepecified
    scrapper.login(username=username, password=password)

    # Scroll to the bottom of page for 10 seconds
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

    # Ends the selenium chrome driver after 60 seconds
    scrapper.end(seconds)


main()
