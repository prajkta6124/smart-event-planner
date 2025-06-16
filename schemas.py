from pydantic import BaseModel
from datetime import date

class EventCreate(BaseModel):
    name: str
    location: str
    date: date
    event_type: str

class EventOut(EventCreate):
    id: int

class WeatherOut(BaseModel):
    location: str
    date: date
    temperature: float
    precipitation: float
    wind_speed: float
    description: str
