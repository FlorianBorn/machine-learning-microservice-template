import numpy as np
import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import RFE
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.pipeline import make_pipeline, make_union
from tpot.builtins import StackingEstimator
from tpot.export_utils import set_param_recursive
from microservice.data.data import load_data

def train_model(X: pd.DataFrame, y: pd.DataFrame):
    '''
    input: 
        X: a DataFrame containing the data neccessary to train the model (must be preprocessed)
        y: the target data (must be preprocessed)
    returns:
        mdl: a trained model object
    '''       
    
    #training_features, testing_features, training_target, testing_target = \
    #            train_test_split(features, tpot_data['target'], random_state=42)

    # Average CV score on the training set was: 0.9729729729729729
    exported_pipeline = make_pipeline(
        StackingEstimator(estimator=SGDClassifier(alpha=0.001, eta0=1.0, fit_intercept=True, l1_ratio=0.0, learning_rate="constant", loss="modified_huber", penalty="elasticnet", power_t=50.0)),
        RFE(estimator=ExtraTreesClassifier(criterion="gini", max_features=0.5, n_estimators=100), step=0.1),
        GaussianNB()
    )
    # Fix random state for all the steps in exported pipeline
    set_param_recursive(exported_pipeline.steps, 'random_state', 42)

    exported_pipeline.fit(X, y)
    return exported_pipeline
