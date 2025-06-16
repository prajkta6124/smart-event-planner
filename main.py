from fastapi import FastAPI, HTTPException
from app.models import Base, Event
from app.schemas import EventCreate
from app.database import SessionLocal, engine
from app.weather import fetch_weather
from app.logic import score_weather
from sqlalchemy.orm import Session

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.post("/events")
def create_event(event: EventCreate):
    db = SessionLocal()
    new_event = Event(**event.dict())
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return new_event

@app.get("/weather/{location}/{date}")
def get_weather(location: str, date: str):
    data = fetch_weather(location)
    for forecast in data['list']:
        if forecast['dt_txt'].startswith(date):
            main = forecast['main']
            weather = forecast['weather'][0]
            wind = forecast['wind']
            return {
                "temperature": main['temp'],
                "precipitation": forecast.get('pop', 0) * 100,
                "wind_speed": wind['speed'],
                "description": weather['description']
            }
    raise HTTPException(status_code=404, detail="Weather data not found")

@app.post("/events/{id}/weather-check")
def weather_check(id: int):
    db = SessionLocal()
    event = db.query(Event).get(id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    weather = get_weather(event.location, event.date.isoformat())
    score = score_weather(weather["temperature"], weather["precipitation"],
                          weather["wind_speed"], event.event_type, weather["description"])
    return {"suitability": score, "weather": weather}
