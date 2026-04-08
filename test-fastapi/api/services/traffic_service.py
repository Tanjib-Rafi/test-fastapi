from sqlalchemy.orm import Session
from typing import List

from models.models import TrafficData
from api.schemas.schemas import TrafficCreate


class TrafficService:

    @staticmethod
    def create_traffic(db: Session, data: TrafficCreate):
        traffic = TrafficData(**data.dict())

        db.add(traffic)
        db.commit()
        db.refresh(traffic)

        return {
            "status": "success",
            "id": traffic.id
        }

    @staticmethod
    def bulk_insert(db: Session, data_list: List[TrafficCreate]):
        objects = [TrafficData(**data.dict()) for data in data_list]

        db.bulk_save_objects(objects)
        db.commit()

        return {
            "status": "success",
            "count": len(objects)
        }