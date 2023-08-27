from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, models
from pprint import pprint
import secrets


def generate_session_id():
    token = secrets.token_hex(16)
    print(token)
    return token


def create(request: schemas.Cart, db: Session):
    session_id = generate_session_id()
    new_cart = models.Cart(
        quantity=request.quantity, product_id=request.product_id, session_id=session_id
    )
    db.add(new_cart)
    db.commit()
    db.refresh(new_cart)
    return new_cart


def get_all(db: Session):
    carts = db.query(models.Cart).all()
    return carts


def destroy(id: int, db: Session):
    cart = db.query(models.Cart).filter(models.Cart.id == id)

    if not cart.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"cart with id {id} not found",
        )

    cart.delete(synchronize_session=False)
    db.commit()
    return "done"


def update(id: int, request: schemas.Cart, db: Session):
    cart = db.query(models.Cart).filter(models.Cart.id == id).first()
    if not cart:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"cart with id {id} not found",
        )

    for attr, value in request.dict().items():
        setattr(cart, attr, value)

    db.commit()
    return "updated"


def show(id: int, db: Session):
    cart = db.query(models.Cart).filter(models.Cart.id == id).first()
    if not cart:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"cart with the id {id} is not available",
        )
    return cart
