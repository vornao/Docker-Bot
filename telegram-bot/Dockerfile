FROM python:3.9-alpine

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

COPY . /app
WORKDIR /app

ENTRYPOINT gunicorn --bind 0.0.0.0:5000 teleflask_bot:appl

