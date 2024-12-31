import sys
import os

# Agregar el directorio raíz del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from ..app import app

client = TestClient(app)

def test_get_api_status():
    response = client.get("/GET_API_STATUS")
    assert response.status_code == 200
    assert response.json() == {"status": "API is running"}

def test_get_customers():
    response = client.get("/GET_CUSTOMERS")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_products():
    response = client.get("/GET_PRODUCTS")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_orders():
    response = client.get("/GET_ORDERS")
    assert response.status_code == 200
    assert len(response.json()) > 0