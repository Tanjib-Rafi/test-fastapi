from fastapi import FastAPI
from api.routers import traffic

app = FastAPI()

app.include_router(traffic.router)