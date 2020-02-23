import sklearn.datasets
import seaborn as sns
import pandas as pd

def load_data() -> pd.DataFrame:
    '''
    This function is meant to be the interface between data engineer and data scientist.
    Ideally, this is the only 'data'-function needed by the data scientist.

    returns:
        a dataframe containing all data and the target
    '''
    df_data = sns.load_dataset('iris')

    return df_data