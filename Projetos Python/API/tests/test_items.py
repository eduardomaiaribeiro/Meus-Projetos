from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Bem-vindo" in response.json()["message"]

def test_read_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_item():
    new_item = {"id": 3, "name": "Monitor", "description": "Monitor 24''", "price": 800.0, "is_offer": False}
    response = client.post("/items/", json=new_item)
    assert response.status_code == 201
    assert response.json()["name"] == "Monitor"

def test_update_item():
    updated_item = {"id": 1, "name": "Teclado Mecânico Atualizado", "description": "Teclado RGB", "price": 260.0, "is_offer": True}
    response = client.put("/items/1", json=updated_item)
    assert response.status_code == 200
    assert response.json()["name"] == "Teclado Mecânico Atualizado"

def test_delete_item():
    response = client.delete("/items/2")
    assert response.status_code == 204
