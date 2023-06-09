from sqlalchemy.orm import Session
from .. import schemas, models




def create(request: schemas.Product, db: Session):
    new_product = models.Product(title=request.title, price=request.price, pictures=request.pictures, status=request.status, description=request.description)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product