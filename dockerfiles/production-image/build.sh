# the name "microservice" should be replaced by a more meaningful name (depending on the project)

cd ..
docker build -t microservice -f dockerfiles/runtime-image/Dockerfile .
cd dockerfiles/runtime-image