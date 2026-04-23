from fastapi import APIRouter, HTTPException
from typing import List
from ..models import Item
from ..database import fake_db

router = APIRouter()

@router.get("/items/", response_model=List[Item], tags=["Itens"])
def read_items():
    return fake_db

@router.get("/items/{item_id}", response_model=Item, tags=["Itens"])
def read_item(item_id: int):
    for item in fake_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item não encontrado")

from fastapi import Body

@router.post(
    "/items/",
    response_model=Item,
    status_code=201,
    tags=["Itens"],
    summary="Cria um novo item",
    response_description="O item criado"
)
def create_item(
    item: Item = Body(
        ...,
        example={
            "id": 3,
            "name": "Monitor",
            "description": "Monitor 24''",
            "price": 800.0,
            "is_offer": False
        }
    )
):
    """
    Cria um novo item no banco de dados.
    """
    for existing_item in fake_db:
        if existing_item.id == item.id:
            raise HTTPException(status_code=400, detail="Item com este ID já existe")
    fake_db.append(item)
    return item

@router.put("/items/{item_id}", response_model=Item, tags=["Itens"])
def update_item(item_id: int, updated_item: Item):
    for i, item in enumerate(fake_db):
        if item.id == item_id:
            if item_id != updated_item.id:
                raise HTTPException(status_code=400, detail="Não é permitido alterar o ID do item na rota PUT")
            fake_db[i] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item não encontrado para atualização")

@router.delete("/items/{item_id}", status_code=204, tags=["Itens"])
def delete_item(item_id: int):
    for i, item in enumerate(fake_db):
        if item.id == item_id:
            del fake_db[i]
            return
    raise HTTPException(status_code=404, detail="Item não encontrado para remoção")
