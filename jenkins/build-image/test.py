# $1 ... image name (which should be tested)
# $2 ... image tag

# Template Imports
import argparse
import docker
import requests
import sys
import json
import time
import logging
from pathlib import Path

# Custom Imports
# ...

logging.basicConfig(format='%(asctime)s, %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%m-%d %H:%M:%S',
                    level=logging.DEBUG)

logging.info("Start Container Tests!")

test_file = "classification1.json" # rename if neccassary
test_subfolder = "prediction"
endpoint = "/api/predictions"
schema = "http" # change if neccessary
host_port = 45000
container_port = 8000

project_root = Path(__file__).resolve().parents[2]

# get CMD args
parser = argparse.ArgumentParser()
parser.add_argument("image_name", type=str, help="The name of the image, which you want to test.")
parser.add_argument("image_tag", type=str, help="The tag of the image, which you want to test.")
args = parser.parse_args()

client = docker.from_env()

## Run the image which we want to test
params = {
        "image": "{}:{}".format(args.image_name, args.image_tag),
        "detach": True,
        "name": "image-test",
        "remove": True
}

container = client.containers.run(**params)
container.reload() 
ip_addr = container.attrs['NetworkSettings']['IPAddress']
logging.debug("Container IP: {}".format(ip_addr))


## Run the test
n_retry = 3
status_code = 0
time.sleep(3)
for i in range(n_retry):
        try:
                with open(str(project_root / "tests" / test_subfolder / test_file), "rb") as fp:
                        test_req = json.load(fp)
                        logging.debug(f"Test Payload: {test_req}")
                response = requests.post(url=f"{schema}://{ip_addr}:{container_port}{endpoint}", json=test_req)
                status_code = response.status_code
                logging.debug(f"Test Response: {response.text}")
                break
        except :
                if i == (n_retry - 1):  
                        container.stop()
                        raise
                time.sleep(3)

# exit & clean up
container.stop()
if status_code != 200:
        sys.exit(1)
else:
        sys.exit(0)
