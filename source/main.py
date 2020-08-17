# from https://fastapi.tiangolo.com/tutorial/first-steps/

# Template Imports
import sys
sys.path.append("source")
from typing import List
from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from source.model.mdl import Model
from source.logging.mongodb_logger import MongoDBLogger
from source.logging.fluentd_logger import FluentdLogger
import pandas as pd
import pickle as pkl
import yaml
from source.api.models import PredictionRequest, PredictionResponse, ProbaPredictionResponse
from source.api import ping, predictions
from dotenv import load_dotenv
from pathlib import Path
import os

app = FastAPI()


@app.on_event("startup")
async def startup():
    #await print("startup!")
    load_dotenv(dotenv_path=str(Path(__file__).resolve().parents[1] / '.env'))
    with open("model_bin/model.pkl", "rb") as fp:
        app.state.model = pkl.load(fp)
    if os.environ["enable_mongodb_logging"] == "True":
        app.state.mongodb_logger = MongoDBLogger(
            client_url=os.environ['mongo_db_url'],
            port=int(os.environ['mongo_db_port']),
            db_name=os.environ['mongo_db_name'],
            collection_name=os.environ['mongodb_logging_collection_name'],
            timezone=os.environ['timezone'])
    if os.environ["enable_fluentd_logging"] == "True":
        app.state.fluentd_logger = FluentdLogger(
            fluentd_url=os.environ['fluentd_url'],
            fluentd_port=int(os.environ['fluentd_port']),
            fluentd_base_log_name=os.environ['fluentd_base_log_name'])

@app.on_event("shutdown")
async def shutdown():
    print("shutdown!")


app.include_router(ping.router)
app.include_router(predictions.router)

