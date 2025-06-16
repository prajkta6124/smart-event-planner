from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    date = Column(Date)
    event_type = Column(String)

class WeatherData(Base):
    __tablename__ = "weather_data"
    id = Column(Integer, primary_key=True)
    location = Column(String)
    date = Column(Date)
    temperature = Column(Float)
    precipitation = Column(Float)
    wind_speed = Column(Float)
    description = Column(String)
