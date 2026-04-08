from fastapi import FastAPI
from api.routers import traffic
from api.database import Base, engine

app = FastAPI()

app.include_router(traffic.router)

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)