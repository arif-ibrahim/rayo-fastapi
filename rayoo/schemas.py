from typing import List
from pydantic import BaseModel
from .constant.enum import Size


class ProductBase(BaseModel):
    title: str
    price: float
    pictures: List[str] = []
    status: bool
    quantity_available: int
    color: List[str] = []
    size: List[Size] = []
    description: str


class Product(ProductBase):
    class Config:
        orm_mode = True


class ShowProduct(ProductBase):
    id: int

    class Config:
        orm_mode = True


class CartBase(BaseModel):
    quantity: int


class Cart(CartBase):
    product_id: int

    class Config:
        orm_mode = True


class ShowCart(CartBase):
    id: int
    product: Product

    class Config:
        orm_mode = True
