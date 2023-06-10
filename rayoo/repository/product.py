from sqlalchemy.orm import Session
from .. import schemas, models




def create(request: schemas.Product, db: Session):
    new_product = models.Product(title=request.title, price=request.price, pictures=request.pictures, status=request.status, quantity=request.quantity, color=request.color, size=request.size, description=request.description)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


def get_all(db: Session):
    products = db.query(models.Product).all()
    print(products)
    return products