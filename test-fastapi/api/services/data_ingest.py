from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from models.models import TrafficData, SessionLocal

app = FastAPI()

class TrafficSchema(BaseModel):
    timestamp: datetime
    location_id: str
    vehicle_count: int
    average_speed: float
    congestion_level: str

@app.post("/traffic-data")
def receive_data(data: TrafficSchema):
    db = SessionLocal()

    traffic = TrafficData(**data.dict())
    db.add(traffic)
    db.commit()

    db.close()

    return {"status": "ok"}