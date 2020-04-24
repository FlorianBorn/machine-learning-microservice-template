import logging
from pymongo import MongoClient

logging.basicConfig(format='%(asctime)s, %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%m-%d %H:%M:%S',
                    level=logging.DEBUG)

logging.info("Start Model Tests!")

class Logger():
    def __init__(self, client="mongodb", port=27017, db_name="ml_service", collection_name="prediction_logs"):
        self.client = client
        self.port = port
        self.db_name = db_name
        self.collection_name = collection_name
        self.client = self._connect(client, port)
        self.is_connected = self._is_connected()

    def _connect(self, client, port):
        try:
            self.client = MongoClient(f'mongodb://{client}:{port}/')
            logging.info(f"Connected to: 'mongodb://{client}:{port}/'")
        except:
            self.client = None
            logging.warning(f"Could not connect to: 'mongodb://{client}:{port}/'")

    def _is_connected(self):
        if self.client:
            return True
        else:
            return False

    def emit_one(self, doc: dict):
        if not self.is_connected:
            self._connect(self.client, self.port)
        if self.is_connected:
            self.client[self.db_name][self.collection_name].insert_one(dict)
        else:
            logging.warning(f"Could not emit log! No connection to DB 'mongodb://{client}:{port}/'")