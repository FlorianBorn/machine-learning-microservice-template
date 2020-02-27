# Template Imports
import sys
sys.path.append("../../")
import logging

from utils.model.model import Model
import pandas as pd

# Custom Imports
# ...

logging.basicConfig(format='%(asctime)s, %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%m-%d %H:%M:%S',
                    level=logging.DEBUG)

logging.info("Start Model Tests!")

# A test request must be specified!
test_request = {
    "sepal_length": "0.5",
    "sepal_width": "0.5",
    "petal_length": "0.5",
    "petal_width": "0.5"
}

logging.debug(f"Test Request: {test_request}")

dummy_request = pd.DataFrame([test_request])
model = Model.load()

try:
    logging.info(f"Test 'predict' Methode")
    prediction = model.predict(dummy_request)
    logging.debug(f"Model Predicted: {prediction}")
except:
    exit(-1)

try:
    logging.info(f"Test 'predict_proba' Methode")
    prediction = model.predict_proba(dummy_request)
    logging.debug(f"Model Predicted: {prediction}")
except:
    exit(-2)

