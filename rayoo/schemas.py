from typing import List
from pydantic import BaseModel, Field
from .constant.enum import Size


class UserBase(BaseModel):
    username: str
    email: str
    password_hash: str
    first_name: str
    last_name: str
    address: str
    phone_number: str


class User(UserBase):
    class Config:
        orm_mode = True


class ShowUser(UserBase):
    id: int

    class Config:
        orm_mode = True


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
    session_id: str

    class Config:
        orm_mode = True
