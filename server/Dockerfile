FROM python:3.7-slim

RUN mkdir /server
WORKDIR /server

COPY ./server/requirements.txt /server
RUN pip install -r requirements.txt

COPY ./server /server




