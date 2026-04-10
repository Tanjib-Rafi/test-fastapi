from sqlalchemy import Column, Integer, Float, String, TIMESTAMP
from api.database import Base

class TrafficData(Base):
    __tablename__ = "traffic_data"
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(TIMESTAMP)
    location_id = Column(String)
    vehicle_count = Column(Integer)
    average_speed = Column(Float)
    congestion_level = Column(String)