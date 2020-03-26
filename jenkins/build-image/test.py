# $1 ... image name
# $2 ... image tag

# Template Imports
import argparse
import docker
import requests
import sys
from pathlib import Path

# Custom Imports
# ...

project_root = sys.path.append(Path(__file__).resolve().parents[2])

# get CMD args
parser = argparse.ArgumentParser()
parser.add_argument("image_name", type=str, help="How should the new image be named?")
parser.add_argument("image_tag", type=str, help="What tag should be given to the new image?")
args = parser.parse_args()

client = docker.from_env()

## Run the image which we want to test
params1 = {
        "image": "{}:{}".format(args.image_name, args.image_tag),
#       "command": "python test.py",
        "detach": True,
        "name": "image-test",
        "ports": {"8000":"45000"}, # Host-Port:Container-Port
        "remove": True
}

container = client.containers.run(**params1)
container.reload() 

## Run the test


}
print(container)
