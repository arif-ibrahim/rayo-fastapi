from typing import List
from pydantic import BaseModel

class ProductBase(BaseModel):
    title: str
    price: float
    pictures: List[str] = []
    status: bool
    description: str

class Product(ProductBase):
    class Config():
        orm_mode = True