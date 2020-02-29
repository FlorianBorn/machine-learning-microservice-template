FROM python:3.8.2-slim

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y install \
	wget \
	curl \
	gcc \
    && rm -rf /var/lib/apt/lists/*    

COPY requirements.txt /microservice/requirements.txt

RUN pip install -r /microservice/requirements.txt

