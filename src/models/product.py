# Modelo de produto usando Pydantic - valida automaticamente os dados de entrada
from pydantic import BaseModel, Field

class Product(BaseModel):
    id: int
    name: str
    category: str
    price: float = Field(gt=0)