# Template Imports

# Custom Imports
### Example:
from sklearn.datasets import load_iris
import pandas as pd
### End Example

class DataLoader():
    '''
    This Class is meant to be the interface between data engineer and data scientist.
    Ideally, this is the only 'Data' Class needed by the Data Scientist.
    '''
    def __init__(self):
        pass

    def load_data(self, n_rows: int=None) -> pd.DataFrame:
        '''
        input:
            n_rows: 
                how many rows of data should be returned? 
                Is used for unit testing the models training method
        returns:
            a dataframe containing all features and the target
        '''
        ### Example:
        #df_data = sns.load_dataset('iris')
        data = load_iris()
        df_data = pd.DataFrame(data.data, columns=data.feature_names)
        df_data["species"] = data.target 
        ### End Example
        return df_data.iloc[:n_rows]