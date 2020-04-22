# Template Imports
import sys
sys.path.append("../../")
import logging

from source.model.mdl import Model
from source.data.data_loader import DataLoader

# Custom Imports
# ...

# Command Line Arguments
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
model.export()