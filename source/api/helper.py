from typing import List
from source.logging.helper import prepare_fluentd_msg
import os


def add_background_tasks(background_tasks, context, request: List[dict], response: List[dict], event_name: str):
    if os.environ["enable_mongodb_logging"] == "True":
        background_tasks.add_task(context.app.state.mongodb_logger.emit_many, response)
    if os.environ["enable_fluentd_logging"] == "True":
        logs = prepare_fluentd_msg(context.app, request, response)
        background_tasks.add_task(context.app.state.fluentd_logger.emit_many, event_name, msgs=logs)


def log_to_mongodb(background_tasks, request, response: List[dict]):
    background_tasks.add_task(request.app.state.mongodb_logger.emit_many, response)

def log_to_efk(background_tasks, request, response: List[dict], event_name: str):
    logs = prepare_fluentd_msg(request.app, request, response)
    background_tasks.add_task(request.app.state.fluentd_logger.emit_many, event_name, msgs=logs)