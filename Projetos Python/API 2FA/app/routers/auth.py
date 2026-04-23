from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import pyotp
from typing import Dict

router = APIRouter()

# Usuários em memória (exemplo)
users_db: Dict[str, Dict] = {
    "user@example.com": {
        "username": "user@example.com",
        "password": "senha123",  # Em produção, use hash!
        "2fa_secret": pyotp.random_base32(),
    }
}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = users_db.get(form_data.username)
    if not user or user["password"] != form_data.password:
        raise HTTPException(status_code=400, detail="Usuário ou senha inválidos")
    return {"access_token": user["username"], "token_type": "bearer"}

@router.post("/2fa-verify")
def verify_2fa(token: str, username: str):
    user = users_db.get(username)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    totp = pyotp.TOTP(user["2fa_secret"])
    if not totp.verify(token):
        raise HTTPException(status_code=401, detail="Token 2FA inválido")
    return {"msg": "2FA verificado com sucesso"}

@router.get("/2fa-secret")
def get_2fa_secret(username: str):
    user = users_db.get(username)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return {"secret": user["2fa_secret"]}
