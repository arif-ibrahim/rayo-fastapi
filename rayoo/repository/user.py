from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, models
from pprint import pprint


def create(request: schemas.User, db: Session):
    new_user = models.User(
        username=request.username,
        email=request.email,
        password_hash=request.password_hash,
        first_name=request.first_name,
        last_name=request.last_name,
        address=request.address,
        phone_number=request.phone_number,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all(db: Session):
    users = db.query(models.User).all()
    return users


def destroy(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id)

    if not user.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} not found",
        )

    user.delete(synchronize_session=False)
    db.commit()
    return "user deleted"


def update(id: int, request: schemas.User, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} not found",
        )

    for attr, value in request.dict().items():
        setattr(user, attr, value)

    db.commit()
    return "user updated successfully"


def show(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with the id {id} is not available",
        )
    return user
