from typing import List
from source.logging.helper import prepare_fluentd_msg
from source.config import enable_fluentd_logging, enable_mongodb_logging

def add_background_tasks(background_tasks, context, request: List[dict], response: List[dict], event_name: str):
    if enable_mongodb_logging:
        background_tasks.add_task(context.app.state.mongodb_logger.emit_many, response)
    if enable_fluentd_logging:
        logs = prepare_fluentd_msg(context.app, request, response)
        background_tasks.add_task(context.app.state.fluentd_logger.emit_many, event_name, msgs=logs)