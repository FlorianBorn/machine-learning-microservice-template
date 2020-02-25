from utils.data.data import load_data
from utils.model.model import Model
from utils.config import default_model_path

def train_and_store_model():
    df_data = load_data()
    model = Model()
    model.train(df_data)
    model.export()

if __name__ == "__main__":
    train_and_store_model()