from sqlalchemy import create_engine, Column, Integer, Float, String, TIMESTAMP
from sqlalchemy.orm import sessionmaker, declarative_base


import os

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class TrafficData(Base):
    __tablename__ = "traffic_data"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(TIMESTAMP)
    location_id = Column(String)
    vehicle_count = Column(Integer)
    average_speed = Column(Float)
    congestion_level = Column(String)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()