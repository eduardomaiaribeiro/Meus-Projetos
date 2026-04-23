from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(
    title="Exemplo de API com FastAPI",
    description="Uma API de exemplo para demonstrar operações CRUD básicas usando FastAPI.",
    version="1.0.0"
)

# Modelo de Dados (Pydantic)
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    is_offer: Optional[bool] = None

# Banco de dados simulado em memória
fake_db: List[Item] = [
    Item(id=1, name="Teclado Mecânico", description="Teclado RGB switch blue", price=250.0, is_offer=True),
    Item(id=2, name="Mouse Gamer", description="Mouse 10000 DPI", price=120.0, is_offer=False),
]

@app.get("/", tags=["Root"])
def read_root():
    """
    Endpoint raiz da API.
    """
    return {"message": "Bem-vindo à API de Exemplo com FastAPI! Acesse /docs para ver a documentação interativa."}

@app.get("/items/", response_model=List[Item], tags=["Itens"])
def read_items():
    """
    Retorna todos os itens do banco de dados.
    """
    return fake_db

@app.get("/items/{item_id}", response_model=Item, tags=["Itens"])
def read_item(item_id: int):
    """
    Busca um item específico pelo seu ID.
    """
    for item in fake_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item não encontrado")

@app.post("/items/", response_model=Item, status_code=201, tags=["Itens"])
def create_item(item: Item):
    """
    Cria um novo item no banco de dados.
    """
    for existing_item in fake_db:
        if existing_item.id == item.id:
            raise HTTPException(status_code=400, detail="Item com este ID já existe")
    
    fake_db.append(item)
    return item

@app.put("/items/{item_id}", response_model=Item, tags=["Itens"])
def update_item(item_id: int, updated_item: Item):
    """
    Atualiza as informações de um item existente pelo ID.
    """
    for i, item in enumerate(fake_db):
        if item.id == item_id:
            if item_id != updated_item.id:
                 raise HTTPException(status_code=400, detail="Não é permitido alterar o ID do item na rota PUT")
            fake_db[i] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item não encontrado para atualização")

@app.delete("/items/{item_id}", status_code=204, tags=["Itens"])
def delete_item(item_id: int):
    """
    Remove um item do banco de dados pelo seu ID.
    """
    for i, item in enumerate(fake_db):
        if item.id == item_id:
            del fake_db[i]
            return
    raise HTTPException(status_code=404, detail="Item não encontrado para remoção")
