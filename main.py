# from https://fastapi.tiangolo.com/tutorial/first-steps/

# Template Imports
import sys
sys.path.append("source")
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from source.model.mdl import Model
from source.logging import Logger
import pandas as pd
import pickle as pkl
import yaml



app = FastAPI()

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

@app.on_event("startup")
async def startup():
    #await print("startup!")
    with open("config.yaml", "r") as fp:
        app.config = yaml.load(fp)
    with open("model_bin/model.pkl", "rb") as fp:
        app.model = pkl.load(fp)
    app.logger = Logger(client_url=app.config['db_url'])

@app.on_event("shutdown")
async def shutdown():
    print(foo)
    print("shutdown!")

@app.get("/api/hello-world")
def read_root():
    return {"Hello": "World"}

@app.post("/api/predictions", response_model=List[PredictionResponse])
def predict(request: List[PredictionRequest]):
    '''
    request can contain 1 or more samples
    '''
    X = prepare_request(request)
    predictions = app.model.predict(X)
    response = [{"class_name": str(p)} for p in predictions] # convert prediction (array) to a list of dicts
    app.logger.emit_many(response)
    return response

@app.post("/api/proba_predictions", response_model=List[ProbaPredictionResponse])
def predict_proba(request: List[PredictionRequest]):
    X = prepare_request(request)
    predictions = app.model.predict_proba(X).tolist()

    # prepare response
    classes = app.model.classes
    response = []
    for p in predictions:
        d = {"class_names": classes, "probabilities": p}
        response.append(d)
    return response

def prepare_request(request: List[PredictionRequest]):
    req = [r.dict() for r in request] # convert list of PredictionRequest objects to a list of dicts
    return pd.DataFrame(req)


