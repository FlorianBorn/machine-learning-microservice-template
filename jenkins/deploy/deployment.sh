# $1 ... image name
# $2 ... image tag
# $3 ... repository
# $4 ... deployment name

helm3 install $4 helm/
if [ $? -eq 0 ]
then
  echo "Successfully created deployment"
else
  echo "Failed to create deployment..."
  echo "Try to update deployment..."
  helm3 upgrade $4 helm/
fi