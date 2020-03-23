FROM python:3.8.2-slim

COPY requirements.txt /microservice/requirements.txt

RUN pip install -r /microservice/requirements.txt

COPY utils main.py /microservice/

COPY model_bin/model.pkl /microservice/model_bin/model.pkl