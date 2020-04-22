import pandas as pd
from source.config import target_label
from sklearn.preprocessing import LabelEncoder
from typing import Tuple


class Preprocessor():
    def __init__(self):
        self.le = LabelEncoder()

    def split_X_y(self, data: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
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
        self.le.fit(y[target_label])

    def process_y(self, y: pd.DataFrame) -> pd.DataFrame:
        '''
        input: 
            takes a DataFrame containing the target data
        return:
            preprocessed data (to be used for train the model)
        '''
        processed_y = self.le.transform(y[target_label])
        processed_y = pd.DataFrame(processed_y, columns=['target'])
        return processed_y    

    # def process_raw(self, X: pd.DataFrame, y: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    #     '''
    #     input: 
    #         takes a complete DataFrame from the Datapipeline as Input
    #     return:
    #         preprocessed data splitted into X and y (to use for training the model)
    #     '''
        
    #     X = data.drop(target_label, axis=1)
    #     y = self.le.fit_transform(data[target_label])
    #     y = pd.DataFrame(y, columns=['target'])
    #     return X, y
    
    # def process_inference(self, X: pd.DataFrame) -> pd.DataFrame:
    #     '''
    #     input: 
    #         takes a DataFrame containing only Features for prediction
    #     return:
    #         preprocessed X to feed into the trained model
    #     '''
    #     processed_X = X
    #     return processed_X

