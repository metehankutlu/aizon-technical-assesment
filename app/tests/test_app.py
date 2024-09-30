import json
from marshmallow import ValidationError
import pytest

from app import app

@pytest.fixture()
def client():
    return app.test_client()

@pytest.fixture()
def runner():
    return app.test_cli_runner()

def get_sample_input():
    return {
        "Material_A_Charged_Amount": 2.0, 
        "Material_B_Charged_Amount": 3.0, 
        "Reactor_Volume": 4.0, 
        "Material_A_Final_Concentration_Previous_Batch": 5.0
    }

def test_validation_required_fields(client):
    required_fields = [
        "Material_A_Charged_Amount",
        "Material_B_Charged_Amount",
        "Reactor_Volume",
        "Material_A_Final_Concentration_Previous_Batch"
    ]

    for field in required_fields:
        payload = get_sample_input()
        del payload[field]

        response = client.post("/predict/", json=payload)
        response_json = response.get_json()

        assert response.status_code == 400
        assert "errors" in response_json
        assert field in response_json["errors"]

def test_validation_data_type(client):
    float_fields = [
        "Material_A_Charged_Amount",
        "Material_B_Charged_Amount",
        "Reactor_Volume",
        "Material_A_Final_Concentration_Previous_Batch"
    ]

    for field in float_fields:
        payload = get_sample_input()
        payload[field] = "invalid"

        response = client.post("/predict/", json=payload)
        response_json = response.get_json()

        assert response.status_code == 400
        assert "errors" in response_json
        assert field in response_json["errors"]

def test_prediction(client):
    payload = get_sample_input()

    response = client.post("/predict/", json=payload)

    assert response.status_code == 200
    
    response_json = response.get_json()

    assert "errors" not in response_json

    assert "label" in response_json
    assert "probability" in response_json