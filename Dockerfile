# syntax=docker/dockerfile:1
FROM python:3.9
RUN apt get update
RUN apt get install chromium
WORKDIR /code/
COPY requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8000
COPY . /code/