# from https://fastapi.tiangolo.com/tutorial/first-steps/

# Template Imports
import sys
sys.path.append("source")
from typing import List
from fastapi import FastAPI, BackgroundTasks
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
    if app.config['enable_logging'] == True:
        app.logger = Logger(client_url=app.config['mongo_db_url'],
            port=app.config['mongo_db_port'],
            db_name=app.config['mongo_db_name'],
            collection_name=app.config['logging_collection_name'],
            timezone=app.config['timezone'])

@app.on_event("shutdown")
async def shutdown():
    print("shutdown!")

@app.get("/api/hello-world")
def read_root():
    return {"Hello": "World"}

@app.post("/api/predictions", response_model=List[PredictionResponse])
def predict(request: List[PredictionRequest], background_tasks: BackgroundTasks):
    '''
    request can contain 1 or more samples
    '''
    X = process_request(request)
    predictions = app.model.predict(X)
    response = [{"class_name": str(p)} for p in predictions] # convert prediction (array) to a list of dicts
    if app.config['enable_logging'] == True:
        background_tasks.add_task(app.logger.emit_many, response)
    return response

@app.post("/api/proba_predictions", response_model=List[ProbaPredictionResponse])
def predict_proba(request: List[PredictionRequest], background_tasks: BackgroundTasks):
    X = process_request(request)
    predictions = app.model.predict_proba(X).tolist()

    # prepare response
    classes = app.model.classes
    response = []
    for p in predictions:
        d = {"class_names": classes, "probabilities": p}
        response.append(d)
    if app.config['enable_logging'] == True:
        background_tasks.add_task(app.logger.emit_many, response)
    return response

def process_request(request: List[PredictionRequest]):
    req = [r.dict() for r in request] # convert a list of PredictionRequest objects to a list of dicts
    return pd.DataFrame(req)


