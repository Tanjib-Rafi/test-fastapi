from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from api.database import get_db
from api.schemas.schemas import TrafficCreate, TrafficBulkCreate, TrafficResponse
from models.models import TrafficData
from api.services.traffic_service import TrafficService

router = APIRouter(prefix="/traffic", tags=["Traffic"])


@router.post("/")
def create_traffic(data: TrafficCreate, db: Session = Depends(get_db)):
    return TrafficService.create_traffic(db, data)


@router.post("/bulk")
def create_bulk(data: TrafficBulkCreate, db: Session = Depends(get_db)):
    return TrafficService.bulk_insert(db, data.data)

@router.get("/health")
def health():
    return {"status": "ok", "message": "Service is running"}


@router.get("/", response_model=List[TrafficResponse])
def get_all_traffic(db: Session = Depends(get_db)):
    data = db.query(TrafficData).order_by(TrafficData.timestamp.desc()).all()
    if not data:
        raise HTTPException(status_code=404, detail="No traffic data found")
    return data