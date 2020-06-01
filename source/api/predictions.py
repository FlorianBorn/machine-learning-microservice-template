from fastapi import APIRouter, BackgroundTasks
from source.api.models import PredictionRequest, PredictionResponse, ProbaPredictionResponse
from source.api.helper import add_background_tasks
from typing import List
import pandas as pd
from starlette.requests import Request
from source.logging.helper import prepare_fluentd_msg, flatten_response

router = APIRouter()


@router.post("/api/predictions", response_model=List[PredictionResponse])
def predict(request: List[PredictionRequest], context: Request, background_tasks: BackgroundTasks):
    '''
    request can contain 1 or more samples
    '''
    X = process_request(request)
    predictions = context.app.state.model.predict(X)
    response = [{"class_name": str(p)} for p in predictions] # convert prediction (array) to a list of dicts
    add_background_tasks(background_tasks, context, request, response, "predict")
    return response


@router.post("/api/proba_predictions", response_model=List[ProbaPredictionResponse])
def predict_proba(request: List[PredictionRequest], context: Request,  background_tasks: BackgroundTasks):
    X = process_request(request)
    predictions = context.app.state.model.predict_proba(X).tolist()

    # prepare response
    classes = context.app.state.model.classes
    response = []
    for p in predictions:
        d = {"class_names": classes, "probabilities": p}
        response.append(d)

    flattened_response = flatten_response(response, n_max=context.app.state.config["log_n_best"])
    add_background_tasks(background_tasks, context, request, flattened_response, "predict_proba")
    return response

def process_request(request: List[PredictionRequest]):
    req = [r.dict() for r in request] # convert a list of PredictionRequest objects to a list of dicts
    return pd.DataFrame(req)
