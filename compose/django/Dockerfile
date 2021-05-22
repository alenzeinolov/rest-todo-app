FROM python:3.8

ENV PYTHONBUFFERED=1


RUN apt-get update && apt-get install build-essential libpq-dev -y

COPY ./requirements .

COPY ./compose/django/start.sh /start.sh

RUN pip install -r /prod.txt --no-cache-dir

WORKDIR /app

COPY . /app
