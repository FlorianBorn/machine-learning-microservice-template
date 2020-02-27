FROM ubuntu:18.04

RUN apt-get update && apt-get install \
    build-essential \
    checkinstall \
    libreadline-gplv2-dev \
    libncursesw5-dev \
    libssl-dev \
    libsqlite3-dev \
    tk-dev \
    libgdbm-dev \
    libc6-dev \
    libbz2-dev \
    libffi-dev \
    zlib1g-dev 

WORKDIR /opt

RUN wget https://www.python.org/ftp/python/3.8.1/Python-3.8.1.tgz && tar xzf Python-3.8.1.tgz

WORKDIR Python-3.8.1

RUN ./configure --enable-optimizations && make altinstall