import pytest
from starlette.testclient import TestClient
import sys
from pathlib import Path
sys.path.append(Path(__file__).resolve().parents[1])

from source.main import app


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client  # testing happens here