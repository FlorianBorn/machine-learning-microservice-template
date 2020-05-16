from pathlib import Path
import pytest
import sys
sys.path.append(Path(__file__).resolve().parents[1])
from source.model.train import Preprocessor
import pandas as pd

def test_split_X_y(unprocessed_df):
    p = Preprocessor()
    x, y = p.split_X_y(unprocessed_df)
    assert type(x) == pd.DataFrame
    assert type(y) == pd.DataFrame
    assert len(x) == len(y)


def test_fit_X(splitted_x_y):
    p = Preprocessor()
    x = splitted_x_y[0]
    r = p.fit_X(x)
    assert r == None


def test_fit_y(splitted_x_y):
    p = Preprocessor()
    y = splitted_x_y[1]
    r = p.fit_y(y)
    assert r == None


def test_process_X(unprocessed_df):
    p = Preprocessor()
    x, y = p.split_X_y(unprocessed_df)
    processed_x = p.process_X(x)
    assert type(processed_x) == pd.DataFrame


def test_process_y(unprocessed_df):
    p = Preprocessor()
    x, y = p.split_X_y(unprocessed_df)
    processed_y = p.process_y(y)
    assert type(processed_y) == pd.DataFrame

