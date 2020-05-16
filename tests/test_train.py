from pathlib import Path
import pytest
import sys
sys.path.append(Path(__file__).resolve().parents[1])
from source.model.train import train_model, get_classes
import pandas as pd

def test_train_model(processed_X, processed_y):
    model = train_model(processed_X, processed_y)
    assert model is not None

# the output of classes should be a list
# if get_classes should be tested depends on the problem 
# being a classication task
# def get_classes():
#    pass
#    assert type(classes) == list
#    assert len(classes) > 0