FROM python:3.7

RUN pip install scrapy google-cloud-firestore Pillow botocore

RUN mkdir -p /src
WORKDIR /src


