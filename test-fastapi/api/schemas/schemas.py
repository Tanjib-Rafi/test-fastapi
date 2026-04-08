from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import List, Literal


class TrafficBase(BaseModel):
    timestamp: datetime
    location_id: str
    vehicle_count: int
    average_speed: float
    congestion_level: Literal["low", "medium", "high"]


class TrafficCreate(TrafficBase):
    pass


# for bulk insert (important for real-time systems)
class TrafficBulkCreate(BaseModel):
    data: List[TrafficCreate]


class TrafficResponse(TrafficBase):
    id: int

    model_config = ConfigDict(from_attributes=True)