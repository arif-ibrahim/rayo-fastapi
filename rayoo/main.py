from fastapi import FastAPI
from . import models
from .database import engine
from .routers import product


app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(product.router)
