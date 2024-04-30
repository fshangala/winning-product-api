# syntax=docker/dockerfile:1
FROM python:3.10-alpine
RUN apk update
RUN apk add chromium
RUN apk add chromium-chromedriver
WORKDIR /code/
COPY requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8000
COPY . /code/