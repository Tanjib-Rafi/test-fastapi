from fastapi import FastAPI
from api.routers import traffic
from models.models import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(traffic.router)