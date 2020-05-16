from starlette import testclient
import json
import pytest
import sys
from pathlib import Path
sys.path.append(Path(__file__).resolve().parents[1])
from source.helper import load_json

path = str(Path(__file__).resolve().parents[1] / "tests/prediction/example_classification1.json")
dummy = load_json(path)
def test_predict(test_app):
    with test_app as t_app:
        response = t_app.post("api/predictions", json=dummy)
        assert response.status_code == 200
        assert "class_name" in response.json()[0] # if 1 response is correct, the others should also be correct