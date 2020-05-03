from pymongo import MongoClient
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1])) 
from source.helper import load_config

config = load_config()
client = MongoClient(host=config["mongo_db_url"], port=config["mongo_db_port"])
db = client.get_database(name=config["mongo_db_name"])
collection = db.get_collection(config["logging_collection_name"])
for doc in collection.find():
    print(doc)