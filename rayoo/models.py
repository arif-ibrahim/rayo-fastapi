from sqlalchemy import (
    Enum as SQLAlchemyEnum,
    Column,
    Integer,
    String,
    Float,
    ARRAY,
    Boolean,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from .constant.enum import Size
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password_hash = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    address = Column(String)
    phone_number = Column(String)


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    price = Column(Float)
    pictures = Column(ARRAY(String))
    status = Column(Boolean)
    quantity_available = Column(Integer)
    color = Column(ARRAY(String))
    size = Column(ARRAY(SQLAlchemyEnum(Size, name="product_size")))
    description = Column(String)
    cart = relationship("Cart", back_populates="product")


class Cart(Base):
    __tablename__ = "carts"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String, index=True)
    quantity = Column(Integer)
    product_id = Column(Integer, ForeignKey("products.id"))
    product = relationship("Product", back_populates="cart", uselist=False)
