from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from api.routers import traffic
from api.database import Base, engine
from models import models

from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Create tables
    Base.metadata.create_all(bind=engine)
    yield
    # Shutdown: (nothing needed for now)

app = FastAPI(lifespan=lifespan)
app.include_router(traffic.router)