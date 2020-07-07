from pymongo import MongoClient
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1])) 
from source.helper import load_config
import os
from dotenv import load_dotenv 
from pathlib import Path

config = load_config()
load_dotenv(dotenv_path=str(Path(__file__).resolve().parents[1] / '.env'))
client = MongoClient(host=os.environ["mongo_db_url"], port=os.environ["mongo_db_port"])
db = client.get_database(name=os.environ["mongo_db_name"])
collection = db.get_collection(os.environ["mongodb_logging_collection_name"])
for doc in collection.find():
    print(doc)