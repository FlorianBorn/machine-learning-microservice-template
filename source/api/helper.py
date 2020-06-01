from typing import List
from source.logging.helper import prepare_fluentd_msg

def add_background_tasks(background_tasks, context, request: List[dict], response: List[dict], event_name: str):
    if context.app.state.config['enable_logging'] == True:
        background_tasks.add_task(context.app.state.mongodb_logger.emit_many, response)
    if context.app.state.config['enable_fluentd_logging'] == True:
        logs = prepare_fluentd_msg(context.app, request, response)
        background_tasks.add_task(context.app.state.fluentd_logger.emit_many, event_name, msgs=logs)