# Template Imports
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2])) # project's root
import logging
from source.model.mdl import Model
from source.helper import load_json, load_config
import pandas as pd

# Custom Imports
# ...

logging.basicConfig(format='%(asctime)s, %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%m-%d %H:%M:%S',
                    level=logging.DEBUG)

logging.info("Start Model Tests!")

config = load_config()
test_case = load_json(config["prediction_test_case_path"])

logging.debug(f"Test Request: {test_case}")

dummy_request = pd.DataFrame(test_case)
model = Model.load()

try:
    logging.info(f"Test 'predict' Methode")
    prediction = model.predict(dummy_request)
    logging.debug(f"Model Predicted: {prediction}")
except:
    raise

try:
    logging.info(f"Test 'predict_proba' Methode")
    prediction = model.predict_proba(dummy_request)
    logging.debug(f"Model Predicted: {prediction}")
except:
    raise

