# $1 ... deployment name
# $2 ... values file

echo "Try to install deployment..."
microk8s.helm3 install $1 -f $2 helm/
if [ $? -eq 0 ]
then
  echo "Successfully created deployment"
else
  echo "Failed to create deployment..."
  echo "Try to update deployment..."
  microk8s.helm3 upgrade $1 -f $2 helm/
fi