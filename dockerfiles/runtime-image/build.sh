cd ../..
docker build --build-arg docker_gid=$(stat -c '%g' /var/run/docker.sock) -t ml_template_runtime_env -f dockerfiles/runtime-image/Dockerfile .
cd dockerfiles/runtime-image
