from fastapi import FastAPI
from . import models
from .database import engine
from .routers import user, product, cart


app = FastAPI()

models.Base.metadata.create_all(engine)


app.include_router(user.router)
app.include_router(product.router)
app.include_router(cart.router)
