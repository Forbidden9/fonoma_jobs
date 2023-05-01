from fastapi.testclient import TestClient
from starlette import status

from main import app
from utils.unittest import data_ok, data_bad_negative, data_bad_status

client = TestClient(app)


# Testing Endpoint - "/api/order/solution"
def test_solution():
    response = client.post("/api/order/solution", json=data_ok)
    assert response.status_code == 200
    assert response.json() == {"total_revenue": 1099.89}


# Testing Endpoint(Validation: Price negative) - "/api/order/solution"
def test_price_negative():
    response = client.post("/api/order/solution", headers={"Content-Type": "application/json"}, json=data_bad_negative)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "You should check that the price of an item 1 can't be negative"}


# Testing Endpoint(Validation: Status empty) - "/api/order/solution"
def test_status_empty():
    response = client.post("/api/order/solution", headers={"Content-Type": "application/json"}, json=data_bad_status)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "You should check that the status of an item 1 can't be empty"}
