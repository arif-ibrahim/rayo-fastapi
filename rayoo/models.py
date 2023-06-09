from sqlalchemy import Column, Integer, String, Float, ARRAY, Boolean
from .database import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    price = Column(Float)
    pictures = Column(ARRAY(String))
    status = Column(Boolean)
    description = Column(String)