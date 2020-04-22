from source.data.data_loader import DataLoader
from source.model.mdl import Model
from source.config import default_model_path

def train_and_store_model():
    df_data = DataLoader().load_data()
    model = Model()
    model.train(df_data)
    model.export()

if __name__ == "__main__":
    train_and_store_model()