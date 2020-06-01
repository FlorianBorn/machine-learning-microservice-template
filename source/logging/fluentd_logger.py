import logging
from fluent import sender
from typing import List
from datetime import datetime
import time

 
logging.basicConfig(format='%(asctime)s, %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%m-%d %H:%M:%S',
                    level=logging.DEBUG)

 
class FluentdLogger():
    def __init__(self,
                fluentd_url: str,
                fluentd_port: int,
                fluentd_base_log_name: str):
 
        self.fluentd_url = fluentd_url
        self.fluentd_port = fluentd_port
        self.fluentd_sender = self.__get_fluent_sender(fluentd_base_log_name, fluentd_url, fluentd_port)

        logging.info(
            f'''
            Initialized EFKLogger:
            Fluentd URL:\t {fluentd_url}
            Fluentd Port:\t {fluentd_port}
            Fluentd BaseLog Name: {fluentd_base_log_name}
            ''')


    def __get_fluent_sender(self, fluentd_base_log_name, fluentd_url, fluentd_port):
        return sender.FluentSender(fluentd_base_log_name, host=fluentd_url, port=fluentd_port)
 

    def emit(self, event_name: str, msg: dict) -> bool:
        msg = self.__add_timestamp(msg)
        self.fluentd_sender.emit(event_name, msg)
        logging.debug(f"\nEmitted Message: {msg}\nEvent Name: {event_name}")
 

    def emit_many(self, event_name: str, msgs: List[dict]) -> bool:
        for msg in msgs:
            msg = self.__add_timestamp(msg)
            self.fluentd_sender.emit_with_time(event_name, int(time.time()), msg)
        logging.debug(f"\nEmitted many messages!\nEvent Name: {event_name}")
 

    def __add_timestamp(self, msg: dict):
        msg['timestamp'] = int(time.time())
        return msg