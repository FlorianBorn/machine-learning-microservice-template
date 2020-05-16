from fastapi import APIRouter, BackgroundTasks
from source.api.models import PredictionRequest, PredictionResponse, ProbaPredictionResponse
from typing import List
import pandas as pd
from starlette.requests import Request

router = APIRouter()


@router.post("/api/predictions", response_model=List[PredictionResponse])
def predict(request: List[PredictionRequest], context: Request, background_tasks: BackgroundTasks):
    '''
    request can contain 1 or more samples
    '''
    X = process_request(request)
    predictions = context.app.state.model.predict(X)
    response = [{"class_name": str(p)} for p in predictions] # convert prediction (array) to a list of dicts
    if context.app.state.config['enable_logging'] == True:
        background_tasks.add_task(context.app.state.logger.emit_many, response)
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
    if context.app.state.config['enable_logging'] == True:
        background_tasks.add_task(context.app.state.logger.emit_many, response)
    return response

def process_request(request: List[PredictionRequest]):
    req = [r.dict() for r in request] # convert a list of PredictionRequest objects to a list of dicts
    return pd.DataFrame(req)