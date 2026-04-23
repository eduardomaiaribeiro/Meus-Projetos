import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_login_success():
    response = client.post("/token", data={"username": "user@example.com", "password": "senha123"})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_login_fail():
    response = client.post("/token", data={"username": "user@example.com", "password": "errada"})
    assert response.status_code == 400

def test_2fa_secret():
    response = client.get("/2fa-secret", params={"username": "user@example.com"})
    assert response.status_code == 200
    assert "secret" in response.json()

def test_2fa_verify():
    # Obter segredo
    secret = client.get("/2fa-secret", params={"username": "user@example.com"}).json()["secret"]
    import pyotp
    token = pyotp.TOTP(secret).now()
    response = client.post("/2fa-verify", params={"username": "user@example.com", "token": token})
    assert response.status_code == 200
    assert response.json()["msg"] == "2FA verificado com sucesso"
