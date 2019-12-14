FROM python:3.6-alpine3.7

# update apk repo
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.7/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.7/community" >> /etc/apk/repositories

COPY . /app

WORKDIR /app

# install chromedriver
RUN apk update
RUN set -xe \ 
    && rm -rvf chromedriver \
    && rm -rvf data.json \
    && apk add chromium chromium-chromedriver

# upgrade pip
RUN pip install --upgrade pip

ENV VIRTUAL_ENV=/venv
RUN python3 -m venv venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip3 install -r requirements.txt

CMD ["python3", "app.py"]