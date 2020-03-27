# $1 ... image name
# $2 ... image tag
# $3 ... repository
docker tag $1:$2 $3/$1:$2
docker push $3/$1:$2