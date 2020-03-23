# $1 ... Image Name
# $2 ... Image Tag

docker build -t $1:$2 -f dockerfiles/production-image/Dockerfile . # must be called from project's root