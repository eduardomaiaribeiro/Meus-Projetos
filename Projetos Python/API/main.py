from fastapi import FastAPI
from app.routers import items

app = FastAPI(
    title="Exemplo de API com FastAPI",
    description="Uma API de exemplo para demonstrar operações CRUD básicas usando FastAPI.",
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

@app.get("/", tags=["Root"])
def read_root():
    """
    Endpoint raiz da API.
    """
    return {"message": "Bem-vindo à API de Exemplo com FastAPI! Acesse /docs para ver a documentação interativa."}

app.include_router(items.router)
