# linkedin-scrapper
Simple selenium web crawler used to fetch information (url to images and videos) from linkedIn and saves it to a file `data.json`

## Guide
To run this application without using docker you need to download a [chromedriver](https://chromedriver.storage.googleapis.com/index.html?path=78.0.3904.105/) for the the system your on and name it `chromedriver` in project directory. Also in app.py you will have to enter your linkedin `username` and `password` in order to log into linkedin

## Running application
* Make sure to have python 3 installed
* Create a virtual environment by running `virtualenv venv -p python3`
* Activate the virtual environment by running `source venv/bin/activate`
* Install required dependencies by running `pip install -r requirements.txt`
* Run the app by running `python app.py`

## Running application in docker
* Build `docker build -t linkedin-scraper:latest .`
* Run `docker run -it -v ./:/app linkedin-scraper:latest`
* SSH into running container (optional) `docker exec -it <container_id> sh`
