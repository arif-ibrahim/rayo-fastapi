from typing import List
from pydantic import BaseModel
from .constant.enum import Size


class ProductBase(BaseModel):
    id: int
    title: str
    price: float
    pictures: List[str] = []
    status: bool
    quantity: int
    color: List[str] = []
    size: List[Size] = []
    description: str


class Product(ProductBase):
    class Config:
        orm_mode = True


class ShowProduct(ProductBase):
    class Config:
        orm_mode = True


class CartBase(BaseModel):
    id: int
    quantity: int


class Cart(CartBase):
    product_id: int

    class Config:
        orm_mode = True


class ShowCart(CartBase):
    product: Product

    class Config:
        orm_mode = True
