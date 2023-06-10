from sqlalchemy import Enum as SQLAlchemyEnum, Column, Integer, String, Float, ARRAY, Boolean
from .constant.enum import Size
from .database import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    price = Column(Float)
    pictures = Column(ARRAY(String))
    status = Column(Boolean)
    quantity = Column(Integer)
    color = Column(ARRAY(String))
    size = Column(ARRAY(SQLAlchemyEnum(Size)))
    description = Column(String)