import pandas as pd
import numpy as np
import pathlib
from .preprocessing import Preprocessor
from .train import train_model


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

    def train(self, raw_data: pd.DataFrame):
        '''
        Trains a model from raw (unprocessed) data from the data pipeline
        input:

        '''
        processed_X, processed_y = self.preprocessor.process_raw(raw_data)
        self.model = train_model(processed_X, processed_y)

    def load(self, path: pathlib.Path):
        '''
        Loads a trained model from path
        input:

        '''
        pass

    def predict(self, X: pd.DataFrame):
        processed_X = self.preprocessor.process_X(X)
        return self.model.predict(processed_X)
        
    def predict_proba(self, X: pd.DataFrame):
        processed_X = self.preprocessor.process_X(X)
        return self.model.predict_proba(processed_X)
