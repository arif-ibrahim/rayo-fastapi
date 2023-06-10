from typing import List
from pydantic import BaseModel
from .constant.enum import Size

class ProductBase(BaseModel):
    title: str
    price: float
    pictures: List[str] = []
    status: bool
    quantity: int
    color: List[str] = []
    size: List[Size] = []
    description: str

class Product(ProductBase):
    class Config():
        orm_mode = True


class ShowProduct(ProductBase):
    class Config():
        orm_mode = True