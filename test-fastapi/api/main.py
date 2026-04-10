from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from api.routers import traffic
from api.database import Base, engine
from models import models

app = FastAPI()
app.include_router(traffic.router)

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)