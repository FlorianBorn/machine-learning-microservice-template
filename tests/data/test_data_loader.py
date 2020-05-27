import pytest
import sys
from pathlib import Path
from source.helper import load_json
sys.path.append(Path(__file__).resolve().parents[2])
from source.data.data_loader import DataLoader
import pandas as pd

def test_load_data():
    dl = DataLoader()
    df = dl.load_data(n_rows=50)
    assert type(df) is pd.DataFrame