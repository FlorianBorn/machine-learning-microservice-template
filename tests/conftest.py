import pytest
from starlette.testclient import TestClient
import sys
from pathlib import Path
from source.helper import load_json
sys.path.append(Path(__file__).resolve().parents[1])
from source.data.data_loader import DataLoader
from source.model.train import Preprocessor

from source.main import app


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client  # testing happens here

@pytest.fixture()
def single_request():
    path = str(Path(__file__).resolve().parents[1] / "tests/prediction/example_classification1.json")
    return load_json(path)


@pytest.fixture()
def batch_request():
    path = str(Path(__file__).resolve().parents[1] / "tests/prediction/batch_request.json")
    return load_json(path)


@pytest.fixture()
def unprocessed_df():
    dl = DataLoader()
    return dl.load_data(50)


@pytest.fixture()
def splitted_x_y(unprocessed_df):
    p = Preprocessor()
    x, y = p.split_X_y(unprocessed_df)
    return x, y

@pytest.fixture()
def processed_X(splitted_x_y):
    p = Preprocessor()
    x = splitted_x_y[0]
    p.fit_X(x)
    return p.process_X(x) 

@pytest.fixture()
def processed_y(splitted_x_y):
    p = Preprocessor()
    y = splitted_x_y[1]
    p.fit_y(y)
    return p.process_X(y) 