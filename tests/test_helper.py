from pathlib import Path
import pytest
import sys
sys.path.append(Path(__file__).resolve().parents[2])
from source.helper import load_config, load_json
import json


def test_load_config():
    config = load_config()
    assert type(config) is dict
    assert len(config) > 0

def test_load_json():
    path = Path(__file__).resolve().parents[0] / "prediction" / "batch_request.json"
    j = load_json(path) 
    # smoke test