
from fastapi import FastAPI, Depends, HTTPException
from app.routers import auth
from fastapi.security import OAuth2PasswordBearer

app = FastAPI(
	title="API 2FA com FastAPI",
	description="API de autenticação com Two-Factor Authentication (2FA) usando FastAPI.",
	version="1.0.0",
	contact={
		"name": "Seu Nome",
		"url": "https://github.com/seuusuario",
		"email": "seu@email.com"
	},
	license_info={
		"name": "MIT",
		"url": "https://opensource.org/licenses/MIT"
	},
	docs_url="/docs",
	redoc_url="/redoc",
	openapi_url="/openapi.json"
)

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
