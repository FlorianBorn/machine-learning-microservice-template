from pydantic import BaseModel
from pathlib import Path
from typing import List
from source.features import input_features, ID_NAME
import yaml

# Create class PredictionRequest dynamically from the models input parameters
attributes = {}
if len(ID_NAME) > 0:
    attributes.update({ID_NAME: ''})
attributes.update({f:'' for f in input_features})
PredictionRequest = type("PredictionRequest", (BaseModel,), attributes) 

class PredictionResponse(BaseModel):
    class_name: str

class ProbaPredictionResponse(BaseModel):
    class_names: List[str]
    probabilities: List[float]