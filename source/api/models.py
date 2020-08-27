from pydantic import BaseModel
from pathlib import Path
from typing import List
from source.features import input_features, ID_NAME
import yaml

# Create class PredictionRequest dynamically from the models input parameters
attributes = {}
if len(ID_NAME) > 0:
    attributes.update({ID_NAME: ''})
# To add the correct type: add a dict type_to_dummy (e.g. {"int": 0, "float": 0.0})
# in featury.py change the features to dict (e.g {"sepal_length": str (or "string")})
attributes.update({f:'' for f in input_features}) 
PredictionRequest = type("PredictionRequest", (BaseModel,), attributes) 

class PredictionResponse(BaseModel):
    class_name: str

class ProbaPredictionResponse(BaseModel):
    class_names: List[str]
    probabilities: List[float]