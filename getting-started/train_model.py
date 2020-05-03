import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))
print(str(Path(__file__).resolve().parents[1]))
from source.data.data_loader import DataLoader
from source.model.mdl import Model

# load data
dl = DataLoader()
df = dl.load_data()
# train and store the model
mdl = Model()
mdl.train(df)
mdl.export()