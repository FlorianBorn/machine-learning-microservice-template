import logging
from typing import List
from pymongo import MongoClient

logging.basicConfig(format='%(asctime)s, %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%m-%d %H:%M:%S',
                    level=logging.DEBUG)
                    

class Logger():
    def __init__(self, client_url="mongodb", port=27017, db_name="ml_service", collection_name="prediction_logs"):
        self.client_url = client_url
        self.port = port
        self.db_name = db_name
        self.collection_name = collection_name
        self.client = self._connect(client_url, port)
        self.is_connected = self._is_connected()

    def _connect(self, client_url, port):
        try:
            logging.info(f"Connected to: 'mongodb://{self.client_url}:{port}/'")
            return MongoClient(f'mongodb://{self.client_url}:{port}/')
        except:
            logging.warning(f"Could not connect to: 'mongodb://{self.client_url}:{port}/'")
            return None
            
    def _is_connected(self):
        if self.client:
            return True
        else:
            return False

    def emit_one(self, doc: dict):
        if not self.is_connected:
            self._connect(self.client, self.port)
        if self.is_connected:
            self.client[self.db_name][self.collection_name].insert_one(doc)
        else:
            logging.warning(f"Could not emit log! No connection to DB 'mongodb://{self.client_url}:{self.port}/'")

    def emit_many(self, docs: List[dict]):
        if not self.is_connected:
            self._connect(self.client, self.port)
        if self.is_connected:
            self.client[self.db_name][self.collection_name].insert_many(docs)
        else:
            logging.warning(f"Could not emit logs! No connection to DB 'mongodb://{self.client_url}:{self.port}/'")
