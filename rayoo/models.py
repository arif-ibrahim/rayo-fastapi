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


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    price = Column(Float)
    pictures = Column(ARRAY(String))
    status = Column(Boolean)
    quantity = Column(Integer)
    color = Column(ARRAY(String))
    size = Column(ARRAY(SQLAlchemyEnum(Size)))
    description = Column(String)
    cart = relationship("Cart", back_populates="product")


class Cart(Base):
    __tablename__ = "carts"

    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer)
    product_id = Column(Integer, ForeignKey("products.id"))
    product = relationship("Product", back_populates="cart", uselist=False)
