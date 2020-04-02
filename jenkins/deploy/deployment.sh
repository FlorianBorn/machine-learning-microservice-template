# $1 ... image name
# $2 ... image tag
# $3 ... repository
# $4 ... deployment name

kubectl create deployment $4 --image=$3/$1:$2
if [ $? -eq 0 ]
then
  echo "Successfully created deployment"
else
  echo "Failed to create deployment..."
  echo "Try to update deployment..."
  kubectl set image deployment $4 $1=$3/$1:$2

