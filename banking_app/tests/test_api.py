from ..main import app
from fastapi.testclient import TestClient
from fastapi import status


client = TestClient(app)

def test_customers_no_query_params():
    response = client.get("/customers")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert isinstance(data, list)


def test_customers_with_min_amount_param():
    response = client.get("/customers?min_amount=10")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert isinstance(data, list)


def test_post_customer_valid_data(valid_body):
    response = client.post("/customers", json=valid_body)
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["name"] == valid_body["name"]
    assert data["surname"] == valid_body["surname"]
    assert data["amount"] == valid_body["amount"]


def test_post_customer_invalid_data(invalid_body):
    response = client.post("/customers", json=invalid_body)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY