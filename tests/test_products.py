# tests/test_products.py - Testes para os endpoints de produtos

import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_get_products():
    response = client.get("/products")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_add_product():
    new_product = {
        "id": 5,
        "name": "Mouse",
        "category": "electronics",
        "price": 50.0,
        "stock": 10
    }
    response = client.post("/products", json=new_product)
    assert response.status_code == 200
    assert response.json()["message"] == "Product added"

def test_get_product():
    response = client.get("/products/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_update_product():
    updated_data = {
        "id": 1,  # ID será ignorado e mantido como 1
        "name": "Updated Laptop",
        "category": "electronics",
        "price": 3200.0,
        "stock": 5
    }
    response = client.put("/products/1", json=updated_data)
    assert response.status_code == 200
    assert response.json()["message"] == "Product updated"

def test_delete_product():
    response = client.delete("/products/5")
    assert response.status_code == 200
    assert response.json()["message"] == "Product deleted"