from typing import List
from .models import Item

# Banco de dados simulado em memória
fake_db: List[Item] = [
    Item(id=1, name="Teclado Mecânico", description="Teclado RGB switch blue", price=250.0, is_offer=True),
    Item(id=2, name="Mouse Gamer", description="Mouse 10000 DPI", price=120.0, is_offer=False),
]
