FROM python:3.7-slim

WORKDIR /home

RUN apt-get update && \
    apt-get install -y curl gcc

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY startup.sh startup.sh

CMD ./startup.sh