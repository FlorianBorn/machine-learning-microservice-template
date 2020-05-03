# Template Imports
import pandas as pd
from source.config import target_label
from typing import Tuple

# Custom Imports


class Preprocessor():
    def __init__(self):
        pass

    def split_X_y(self, data: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
        '''
        Splits the data from the datapipeline into X and y

        input: 
            data: a DataFrame containing all features and target data
        return:
            X: all features
            y: target data
        '''
        ### Example:
        X = data.drop(target_label, axis=1)
        y = pd.DataFrame(data["species"])
        ### End Example
        return X, y

    def fit_X(self, X: pd.DataFrame) -> pd.DataFrame:
        '''
        input: 
            takes a DataFrame containing all features as input
        '''
        pass

    def process_X(self, X: pd.DataFrame) -> pd.DataFrame:
        '''
        input: 
            takes a DataFrame containing all features as input
        return:
            preprocessed data (to be used by the model)
        '''
        ### Example:
        processed_X = X
        ### End Example
        return processed_X

    def fit_y(self, y: pd.DataFrame) -> pd.DataFrame:
        '''
        input: 
            takes a DataFrame containing the target data
        '''
        pass

    def process_y(self, y: pd.DataFrame) -> pd.DataFrame:
        '''
        input: 
            takes a DataFrame containing the target data
        return:
            preprocessed data (to be used for train the model)
        '''
        ### Example:
        processed_y = y
        ### End Example
        return processed_y    


def train_model(X_processed, y_processed):
    ### Example:
    from sklearn.dummy import DummyClassifier
    model = DummyClassifier().fit(X_processed, y_processed)
    ### End Example
    return model

def get_classes(model):
    ### Example:
    classes = [str(c) for c in self.model.classes_] # set classes; classes are needed later while predicting probabilities
    ### End Example
    return classes