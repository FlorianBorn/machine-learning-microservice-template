from source.data.data_loader import DataLoader
from source.model.mdl import Model
from source.config import default_model_path
from pathlib import Path
import yaml


def load_config():
    config_path = Path(__file__).resolve().parents[1]
    with open(str(config_path / "config.yaml"), "r") as fp:
        config = yaml.load(fp)
    return config    

def train_and_store_model():
    df_data = DataLoader().load_data()
    model = Model()
    model.train(df_data)
    model.export()

if __name__ == "__main__":
    train_and_store_model()