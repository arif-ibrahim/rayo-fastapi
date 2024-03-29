from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, models
from pprint import pprint


def create(request: schemas.Product, db: Session):
    new_product = models.Product(
        title=request.title,
        price=request.price,
        pictures=request.pictures,
        status=request.status,
        quantity_available=request.quantity_available,
        color=request.color,
        size=request.size,
        description=request.description,
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


def get_all(db: Session):
    products = db.query(models.Product).all()
    return products


def destroy(id: int, db: Session):
    product = db.query(models.Product).filter(models.Product.id == id)

    if not product.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with id {id} not found",
        )

    product.delete(synchronize_session=False)
    db.commit()
    return "done"


def update(id: int, request: schemas.Product, db: Session):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with id {id} not found",
        )

    for attr, value in request.dict().items():
        setattr(product, attr, value)

    db.commit()
    return "updated"


def show(id: int, db: Session):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with the id {id} is not available",
        )
    return product
