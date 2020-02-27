# Template Imports
import sys
sys.path.append("../../")
import logging

from utils.model.model import Model
from utils.data.data import DataLoader

# Custom Imports
# ...

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