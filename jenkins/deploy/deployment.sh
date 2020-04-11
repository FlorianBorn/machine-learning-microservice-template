# $1 ... image name
# $2 ... image tag
# $3 ... repository
# $4 ... deployment name

microk8s.helm install $4 helm/
if [ $? -eq 0 ]
then
  echo "Successfully created deployment"
else
  echo "Failed to create deployment..."
  echo "Try to update deployment..."
  microk8s.helm upgrade $4 helm/
fi