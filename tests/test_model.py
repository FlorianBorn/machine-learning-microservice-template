from pathlib import Path
import pytest
import sys
sys.path.append(Path(__file__).resolve().parents[1])
from source.model.mdl import Model


def test_train(unprocessed_df):
    mdl = Model()
    r = mdl.train(unprocessed_df)
    assert r is None
    assert mdl.model is not None