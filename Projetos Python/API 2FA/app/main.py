
from fastapi import FastAPI, Depends, HTTPException
from app.routers import auth
from fastapi.security import OAuth2PasswordBearer

app = FastAPI(title="API 2FA com FastAPI")

app.include_router(auth.router)

# Rota pública
@app.get("/public")
def public_route():
	return {"msg": "Rota pública acessível"}

# Rota protegida (exemplo)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

@app.get("/protected")
def protected_route(token: str = Depends(oauth2_scheme)):
	# Aqui você pode validar o token e o 2FA conforme necessário
	if not token:
		raise HTTPException(status_code=401, detail="Token ausente ou inválido")
	return {"msg": "Acesso autorizado à rota protegida"}
