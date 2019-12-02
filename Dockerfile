FROM selenium/standalone-chrome:latest

COPY . /app

WORKDIR /app

ENV SHELL=/bin/bash

RUN sudo apt-get update && sudo apt-get install python python-dev virtualenv python3-pip \
    rm -rf /var/cache/apk/*

RUN virtualenv venv -p python3 \
    source ./venv/bin/activate

CMD [ "python", "app.py"]
