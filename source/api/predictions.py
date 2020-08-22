from fastapi import APIRouter, BackgroundTasks
from source.api.models import PredictionRequest, PredictionResponse, ProbaPredictionResponse
from source.api.helper import add_background_tasks, log_to_mongodb, log_to_efk
from typing import List
import pandas as pd
from starlette.requests import Request
from source.logging.helper import prepare_fluentd_msg, flatten_response
from source.features import task
import os
from dotenv import load_dotenv 
from pathlib import Path

router = APIRouter()


@router.post("/api/predictions", response_model=List[PredictionResponse])
def predict(request: List[PredictionRequest], context: Request, background_tasks: BackgroundTasks):
    '''
    request can contain 1 or more samples
    '''
    X = process_request(request)
    predictions = context.app.state.model.predict(X)
    response = [{"class_name": str(p)} for p in predictions] # convert prediction (array) to a list of dicts

    # start background tasks
    if os.environ["enable_fluentd_logging"] == "True":
        event_name = "predict"
        flattened_response = flatten_response(response, n_max=int(os.environ["fluentd_log_n_best"]))
        log_to_efk(background_tasks, request, flattened_response, event_name)
    if os.environ["enable_mongodb_logging"] == "True":
        log_to_mongodb(background_tasks, request, response)

    return response

if task == "classification":
    @router.post("/api/proba_predictions", response_model=List[ProbaPredictionResponse])
    def predict_proba(body: List[PredictionRequest], request: Request,  background_tasks: BackgroundTasks):
        load_dotenv(dotenv_path=str(Path(__file__).resolve().parents[1] / '.env'))
        X = process_request(body)
        predictions = request.app.state.model.predict_proba(X).tolist()

        # prepare response
        classes = [str(class_) for class_ in request.app.state.model.classes] # convert classes to string, if they are not already strings
        response = []
        for p in predictions:
            d = {"class_names": classes, "probabilities": p}
            response.append(d)

        # start background tasks
        if os.environ["enable_fluentd_logging"] == "True":
            event_name = "predict_proba"
            flattened_response = flatten_response(response, n_max=int(os.environ["fluentd_log_n_best"]))
            log_to_efk(background_tasks, request, flattened_response, event_name)
        if os.environ["enable_mongodb_logging"] == "True":
            log_to_mongodb(background_tasks, request, response)
        
        return response

def process_request(body: List[PredictionRequest]):
    req = [r.dict() for r in body] # convert a list of PredictionRequest objects to a list of dicts
    return pd.DataFrame(req)
