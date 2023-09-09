from typing import List
from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from .. import database, schemas
from ..repository import product


router = APIRouter(prefix="/order", tags=["Orders"])

get_db = database.get_db


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Order, db: Session = Depends(get_db)):
    return product.create(request, db)
