import logging
from typing import List, Union
from pymongo import MongoClient
from datetime import datetime
import pytz

logging.basicConfig(format='%(asctime)s, %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%m-%d %H:%M:%S',
                    level=logging.DEBUG)


class MongoDBLogger():
    def __init__(self, client_url="mongodb", port=27017, db_name="ml_service", collection_name="prediction_logs", timezone:str="GMT"):
        
        logging.info(f'''Initialize Logger - Given Arguments:
            Client URL: {client_url}
            Port: {port}
            DB-Name: {db_name}
            Collection Name: {collection_name}
            Timezone: {timezone}
        ''')
        self.client_url = client_url
        self.port = port
        self.db_name = db_name
        self.collection_name = collection_name
        self.client = self._connect(client_url, port)
        self.is_connected = self._is_connected()
        self.timezone = timezone

    def _connect(self, client_url, port):
        try:
            client = MongoClient(f'mongodb://{self.client_url}:{port}/')
            logging.info(f"Connected to: 'mongodb://{self.client_url}:{port}/'")
            return client
        except:
            logging.warning(f"Could not connect to: 'mongodb://{self.client_url}:{port}/'")
            return None
            
    def _is_connected(self):
        if self.client: return True
        else: return False

    def emit_one(self, doc: dict, add_timestamp: bool=True):
        if not self.is_connected: self._connect(self.client, self.port)
        if not self.is_connected:
            logging.warning(f"Could not emit log! No connection to DB 'mongodb://{self.client_url}:{self.port}/'")
            return
        if add_timestamp == True: 
            doc = self._add_timestamp(doc, self.timezone) 
        self.client[self.db_name][self.collection_name].insert_one(doc)

    def emit_many(self, docs: List[dict], add_timestamp: bool=True):
        if not self.is_connected: self._connect(self.client, self.port)
        if not self.is_connected:
            logging.warning(f"Could not emit logs! No connection to DB 'mongodb://{self.client_url}:{self.port}/'")
            return
        if add_timestamp == True: 
            docs = self._add_timestamp(docs, self.timezone) 
        self.client[self.db_name][self.collection_name].insert_many(docs)
        
    def _add_timestamp(self, doc: Union[list, dict], timezone: str):
        now = self._get_dt_from_timezone(timezone)
        t = type(doc)
        if t == dict:
            doc['timestamp'] = now
        elif t == list:
            for d in doc:
                d['timestamp'] = now
        return doc

    def _get_dt_from_timezone(self, timezone):
        tz = pytz.timezone(timezone)
        return datetime.now(tz)