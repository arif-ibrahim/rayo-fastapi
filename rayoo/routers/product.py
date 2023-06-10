from typing import List
from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from .. import database, schemas
from ..repository import product


router = APIRouter(prefix="/product", tags=["Products"])

get_db = database.get_db


@router.get("/", response_model=List[schemas.ShowProduct])
def all(db: Session = Depends(get_db)):
    return product.get_all(db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Product, db: Session = Depends(get_db)):
    return product.create(request, db)


@router.get("/{id}", response_model=schemas.ShowProduct)
def show(id: int, db: Session = Depends(get_db)):
    return product.show(id, db)
