# Template Imports
import pandas as pd
import pathlib
import pickle as pkl
import uuid
from datetime import datetime
from source.defaults import default_model_path, default_model_name
from source.features import task
from .train import train_model, Preprocessor, get_classes

# Custom Imports
# ...


class Model():
    '''
    The Model class is meant to be the interface between the data scientist and the
    machine learning engineer.
    Ideally, the machine learning engineer only needs to know about the Model class and it's methods,
    but not about how the final model is working internally.
    '''
    def __init__(self):
        self.model = None
        self.preprocessor = Preprocessor()
        self.classes = None
        self.id = self.get_uuid()
        self.creation_time = self.get_str_timestamp()

    def train(self, raw_data: pd.DataFrame):
        '''
        Trains a model from raw (unprocessed) data from the data pipeline
        input:

        '''
        # preprocessing
        X, y = self.preprocessor.split_X_y(raw_data)
        self.preprocessor.fit_X(X)
        self.preprocessor.fit_y(y)
        processed_X = self.preprocessor.process_X(X)
        processed_y = self.preprocessor.process_y(y)

        # fitting
        self.model = train_model(processed_X, processed_y)
        if task == "classification": # if task is classification, get_classes function must be implemented (see train.py)!
            self.classes = get_classes(self.model)

    def predict(self, X: pd.DataFrame):
        processed_X = self.preprocessor.process_X(X)
        return self.model.predict(processed_X)
        
    def predict_proba(self, X: pd.DataFrame):
        processed_X = self.preprocessor.process_X(X)
        return self.model.predict_proba(processed_X)

    @classmethod
    def load(cls, path:str=None):
        '''
        Loads a Model Object from storage.
        '''
        if path == None:
            path = str(default_model_path)
        with open(f"{path}", "rb") as fp:
            model = pkl.load(fp) # model must be pickle file
        return model

    def load_model(self, path:str=None):
        '''
        Loads a trained model-Object (class Model) from path
        input:
            path: path where the model is stored
            name: the name of the actual model file (incl. file ending)
        '''
        if path == None:
            path = str(default_model_path)
        with open(f"{path}", "rb") as fp:
            self.model = pkl.load(fp) # model must be pickle file


    def export_model(self, path:str=None):
        if path == None:
            path = str(default_model_path)        
        with open(f"{path}", "wb") as fp:
            pkl.dump(self.model, fp)

    def export(self, path:str=None):
        if path == None:
            path = str(default_model_path)
        with open(f"{path}", "wb") as fp:
            pkl.dump(self, fp)

    def get_str_timestamp(self):
        return datetime.now().strftime("%Y.%m.%d %H:%M:%S")

    def get_uuid(self):
        return str(uuid.uuid4())