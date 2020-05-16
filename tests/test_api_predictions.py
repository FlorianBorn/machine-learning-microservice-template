from starlette import testclient
import json
import pytest
import sys


def test_predict_single_request(test_app, single_request):
    with test_app as t_app:
        response = t_app.post("api/predictions", json=single_request)
        assert response.status_code == 200
        assert "class_name" in response.json()[0]


def test_predict_batch_request(test_app, batch_request):
    with test_app as t_app:
        response = t_app.post("api/predictions", json=batch_request)
        assert response.status_code == 200
        for r in response.json():
            assert "class_name"  in r 


def test_predict_proba_single_request(test_app, single_request):
    with test_app as t_app:
        response = t_app.post("api/proba_predictions", json=single_request)
        assert response.status_code == 200
        assert "class_names" in response.json()[0]


def test_predict_proba_batch_request(test_app, batch_request):
    with test_app as t_app:
        response = t_app.post("api/proba_predictions", json=batch_request)
        assert response.status_code == 200
        for r in response.json():
            assert "class_names"  in r # if 1 response is correct, the others should also be correct