FROM python:2.7

RUN pip install scrapy

RUN mkdir -p /src
WORKDIR /src


