HOST_PORT=${1:-27017}
docker run --name mongo -d -p $HOST_PORT:27017 mongo:4.2.6-bionic