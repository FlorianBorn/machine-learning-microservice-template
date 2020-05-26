# from https://fastapi.tiangolo.com/tutorial/first-steps/

# Template Imports
import sys
sys.path.append("source")
from typing import List
from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from source.model.mdl import Model
from source.logging.logging import Logger
import pandas as pd
import pickle as pkl
import yaml
from source.api.models import PredictionRequest, PredictionResponse, ProbaPredictionResponse
from source.api import ping, predictions

app = FastAPI()


@app.on_event("startup")
async def startup():
    #await print("startup!")
    with open("config.yaml", "r") as fp:
        app.state.config = yaml.load(fp)
    with open("model_bin/model.pkl", "rb") as fp:
        app.state.model = pkl.load(fp)
    if app.state.config['enable_logging'] == True:
        app.state.logger = Logger(client_url=app.state.config['mongo_db_url'],
            port=app.state.config['mongo_db_port'],
            db_name=app.state.config['mongo_db_name'],
            collection_name=app.state.config['logging_collection_name'],
            timezone=app.state.config['timezone'])


@app.on_event("shutdown")
async def shutdown():
    print("shutdown!")


app.include_router(ping.router)
app.include_router(predictions.router)

