from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from . import models
from .database import engine
from .routers import user, product, cart, file


app = FastAPI()


app.mount("/public", StaticFiles(directory="static"), name="static")


models.Base.metadata.create_all(engine)


app.include_router(user.router)
app.include_router(product.router)
app.include_router(cart.router)
app.include_router(file.router)
