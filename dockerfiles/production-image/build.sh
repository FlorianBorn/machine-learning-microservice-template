#!/bin/bash
# the name "image_version" should be replaced by a more meaningful name (depending on the project)

cd ../..
image_name=$1 # e.g. prod_ml_microservice
image_version=$2 # e.g. 0.0.1
docker build -t "${image_name}:${image_version}" -f dockerfiles/production-image/Dockerfile .
cd dockerfiles/runtime-image