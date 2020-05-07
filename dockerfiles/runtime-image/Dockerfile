FROM python:3.7.7-slim

ARG docker_gid

RUN groupadd -g $docker_gid docker

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y install \
	wget \
	curl \
	gcc \
	docker.io \
    && rm -rf /var/lib/apt/lists/*    

COPY requirements.txt requirements_additional.txt /microservice/

RUN pip install -r /microservice/requirements.txt -r /microservice/requirements_additional.txt
RUN pip install pylint docker




