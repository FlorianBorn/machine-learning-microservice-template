from starlette.testclient import TestClient
from pathlib import Path
import pytest
import sys
sys.path.append(Path(__file__).resolve().parents[1])

from source.main import app

client = TestClient(app)

def test_ping(test_app):
    response = test_app.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong"}