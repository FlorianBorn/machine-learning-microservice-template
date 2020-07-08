# Template Imports
import argparse
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parents[2])) # project's root
import logging
from source.model.mdl import Model
from source.data.data_loader import DataLoader

# Custom Imports
# ...

# Command Line Arguments
parser = argparse.ArgumentParser()
parser.add_argument("--model_path", type=str, help="The full path and file name, where you want to export the trained model to. E.g. /foo/model.pkl")
args = parser.parse_args()
# ToDo - Allow passing cmd line args, e.g. for specifying the path to store the model

logging.basicConfig(format='%(asctime)s, %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%m-%d %H:%M:%S',
                    level=logging.DEBUG)

logging.info("Start Model Training!")

# Load data
dl = DataLoader()
df_data = dl.load_data()

# Train model
model = Model()
model.train(df_data)

# Store trained model
model.export(args.model_path)