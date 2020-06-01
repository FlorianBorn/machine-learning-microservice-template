from pydantic import BaseModel
from source.helper import load_config
from pathlib import Path
from typing import List
import yaml

def load_yaml():
    root = Path(__file__).resolve().parents[2]
    with open(str(root / "source" / "model" / "features.yaml"), "r") as fp:
        y = yaml.load(fp)
    return y   

# Create class PredictionRequest dynamically from the models input parameters
y = load_yaml()
config = load_config()

attributes = {}
if len(config["ID_NAME"]) > 0:
    attributes.update({config["ID_NAME"]: ''})
attributes.update({f:'' for f in y["input_features"]})
PredictionRequest = type("PredictionRequest", (BaseModel,), attributes) 

class PredictionResponse(BaseModel):
    class_name: str

class ProbaPredictionResponse(BaseModel):
    class_names: List[str]
    probabilities: List[float]