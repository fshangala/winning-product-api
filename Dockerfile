# syntax=docker/dockerfile:1
FROM python:3.9
WORKDIR /code/
COPY . /code/
RUN pip install -r requirements.txt
RUN rm -f db.sqlite3
RUN python manage.py migrate
RUN python manage.py createsuperuser --no-input
EXPOSE 8000