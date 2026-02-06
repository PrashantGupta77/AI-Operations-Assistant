import os
from dotenv import load_dotenv
import requests

load_dotenv()


WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")


def get_current_weather(city: str) -> dict:
    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "units": "metric"
    }
    response = requests.get(WEATHER_API_URL, params=params)

    if response.status_code != 200:
        raise Exception(f"Weather API error: {response.status_code}")

    data = response.json()

    weather_info = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"]
    }

    return weather_info