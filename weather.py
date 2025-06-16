import requests
from os import getenv

API_KEY = getenv("WEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

def fetch_weather(location: str):
    params = {
        "q": location,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    return response.json()
