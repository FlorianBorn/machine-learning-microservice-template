from typing import List
from source.helper import load_config

def update_responses(responses: List[dict], new_fields: List[dict]):
    return [dict(**response, **new) for response, new in zip(responses, new_fields)]


def prepare_fluentd_msg(app, requests: List[dict], responses: List[dict], flatten=False, n_max=3):
    tmp_responses = responses.copy()
    config = load_config()
    model_id = app.state.model.id
    model_creation_time = app.state.model.creation_time
    new_fields = [{
        "model_id": model_id, 
        "model_creation_time": model_creation_time}
        for _ in tmp_responses]
    if len(config["ID_NAME"]) > 0:
        for d, r in zip(new_fields, requests):
            d.update({config["ID_NAME"]: r.dict()[config["ID_NAME"]]})
    if flatten:
        tmp_responses = flatten_response(responses, n_max=config["log_n_best"])
    return update_responses(tmp_responses, new_fields)


def flatten_response(responses, n_max=None, sort=True):
    flattened_responses = []
    class_prefix = "class"
    proba_prefix = "proba" 
    if sort:
        assert n_max != None
        responses = sort_n_max(responses, n_max)
    for response in responses:
        flattened_response = {}
        for i, (cl, p) in enumerate(zip(response["class_names"], response["probabilities"]), start=1):
            flattened_response[f"{class_prefix}_{i}"] = cl
            flattened_response[f"{proba_prefix}_{i}"] = p
        flattened_responses.append(flattened_response)
    return flattened_responses


def sort_n_max(responses: List[dict], n_max: int):
    sorted_responses = []
    for response in responses:
        sort = sorted(zip(response["probabilities"], response["class_names"]), reverse=True)
        sort = sort[:n_max]
        sorted_response = {
            "class_names": [c for _,c in sort],
            "probabilities": [p for p,_ in sort]
            }
        sorted_responses.append(sorted_response)
    return sorted_responses
    
