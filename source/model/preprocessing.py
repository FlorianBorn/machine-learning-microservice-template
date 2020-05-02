# Template Imports
import pandas as pd
from source.config import target_label
from sklearn.preprocessing import LabelEncoder
from typing import Tuple

# Custom Imports


class Preprocessor():
    def __init__(self):
        pass

    def split_X_y(self, data: pd.DataFrame, target_label:str) -> Tuple[pd.DataFrame, pd.DataFrame]:
        '''
        Splits the data from the datapipeline into X and y

        input: 
            data: a DataFrame containing all features and target data
        return:
            X: all features
            y: target data
        '''
        X = data.drop(target_label, axis=1)
        y = pd.DataFrame(data[target_label])
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
        processed_X = X
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
        processed_y = y
        return processed_y    
