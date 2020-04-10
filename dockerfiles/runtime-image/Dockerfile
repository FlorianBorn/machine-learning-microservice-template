FROM python:3.8.2-slim

ARG docker_gid

RUN groupadd -g $docker_gid docker

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y install \
	wget \
	curl \
	gcc \
	docker.io \
    && rm -rf /var/lib/apt/lists/*    

COPY requirements.txt /microservice/requirements.txt

RUN pip install -r /microservice/requirements.txt
RUN pip install pylint docker




