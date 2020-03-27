# from https://fastapi.tiangolo.com/tutorial/first-steps/
import sys
sys.path.append("utils")
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from utils.model.mdl import Model
import pandas as pd
import pickle as pkl



app = FastAPI()

# load model
with open("model_bin/model.pkl", "rb") as fp:
    model = pkl.load(fp)

# define Request-Parameter
class PredictionRequest(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class PredictionResponse(BaseModel):
    class_name: str

class ProbaPredictionResponse(BaseModel):
    class_names: List[str]
    probabilities: List[float]


@app.get("/api/hello-world")
def read_root():
    return {"Hello": "World"}

@app.post("/api/predictions", response_model=List[PredictionResponse])
def predict(request: List[PredictionRequest]):
    '''
    request can contain 1 or more samples
    '''
    X = prepare_request(request)
    predictions = model.predict(X)
    response = [{"class_name": str(p)} for p in predictions] # convert prediction (array) to a list of dicts
    return response

@app.post("/api/proba_predictions", response_model=List[ProbaPredictionResponse])
def predict_proba(request: List[PredictionRequest]):
    X = prepare_request(request)
    predictions = model.predict_proba(X).tolist()

    # prepare response
    classes = model.classes
    response = []
    for p in predictions:
        d = {"class_names": classes, "probabilities": p}
        response.append(d)
    return response

def prepare_request(request: List[PredictionRequest]):
    req = [r.dict() for r in request] # convert list of PredictionRequest objects to a list of dicts
    return pd.DataFrame(req)


