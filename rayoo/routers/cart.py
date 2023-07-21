from typing import List
from fastapi import APIRouter, status, Depends
from .. import database, schemas
from sqlalchemy.orm import Session
from ..repository import cart


router = APIRouter(prefix="/cart", tags=["Carts"])

get_db = database.get_db


@router.get("/", response_model=List[schemas.ShowCart])
def all(db: Session = Depends(get_db)):
    return cart.get_all(db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Cart, db: Session = Depends(get_db)):
    return cart.create(request, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(
    id: int,
    db: Session = Depends(get_db),
):
    return cart.destroy(id, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(
    id: int,
    request: schemas.Cart,
    db: Session = Depends(get_db),
):
    return cart.update(id, request, db)


@router.get("/{id}", response_model=schemas.ShowCart)
def show(id: int, db: Session = Depends(get_db)):
    return cart.show(id, db)
