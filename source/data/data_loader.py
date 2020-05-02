# Template Imports

# Custom Imports
import sklearn.datasets
import seaborn as sns
import pandas as pd

class DataLoader():
    '''
    This Class is meant to be the interface between data engineer and data scientist.
    Ideally, this is the only 'Data' Class needed by the Data Scientist.
    '''
    def __init__(self):
        pass

    def load_data(self) -> pd.DataFrame:
        '''
        returns:
            a dataframe containing all features and the target
        '''
        ### Example:
        df_data = sns.load_dataset('iris')
        ### End Example
        return df_data