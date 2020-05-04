cd ../..
image_name=$(grep 'runtime_image_name' config.yaml | awk '{ print $2 }')
image_tag=$(grep 'runtime_image_tag' config.yaml | awk '{ print $2 }')
docker build --build-arg docker_gid=$(stat -c '%g' /var/run/docker.sock) -t $image_name:$image_tag -f dockerfiles/runtime-image/Dockerfile .
cd dockerfiles/runtime-image
