import pandas as pd
import numpy as np
import pathlib
import pickle as pkl
from .preprocessing import Preprocessor
from .train import train_model
from utils.config import default_model_path


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
        #self.default_model_path = pathlib.Path(__file__).resolve().parents[2] / "model_bin" / "model.pkl"
        self.classes = None

    def train(self, raw_data: pd.DataFrame):
        '''
        Trains a model from raw (unprocessed) data from the data pipeline
        input:

        '''
        X, y = self.preprocessor.split_X_y(raw_data)
        self.preprocessor.fit_X(X)
        self.preprocessor.fit_y(y)
        processed_X = self.preprocessor.process_X(X)
        processed_y = self.preprocessor.process_y(y)

        self.model = train_model(processed_X, processed_y)
        self.classes = [str(c) for c in self.model.classes_] # set classes; classes are needed later while predicting probabilities

    def predict(self, X: pd.DataFrame):
        processed_X = self.preprocessor.process_X(X)
        return self.model.predict(processed_X)
        
    def predict_proba(self, X: pd.DataFrame):
        processed_X = self.preprocessor.process_X(X)
        return self.model.predict_proba(processed_X)

    def load(self, path: pathlib.Path=None):
        '''
        Loads a trained model from path
        input:

        '''
        if path is None:
            path = default_model_path
        with open(str(path), "rb") as fp:
            self.model = pkl.load(fp)

    def export_model(self, path: pathlib.Path=None):
        if path is None:
            path = default_model_path
        with open(str(path), "wb") as fp:
            pkl.dump(self.model, fp)

    def export(self, path: pathlib.Path=None):
        if path is None:
            path = default_model_path
        with open(str(path), "wb") as fp:
            pkl.dump(self, fp)