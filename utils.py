import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")


def get_weather(city):

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:

        response = requests.get(
            url,
            params=params
        )

        data = response.json()

        if response.status_code == 200:

            weather_data = {

                "city": data["name"],

                "temperature":
                    data["main"]["temp"],

                "feels_like":
                    data["main"]["feels_like"],

                "humidity":
                    data["main"]["humidity"],

                "pressure":
                    data["main"]["pressure"],

                "weather":
                    data["weather"][0]["description"],

                "wind_speed":
                    data["wind"]["speed"],

                "visibility":
                    data.get("visibility", 0) / 1000
            }

            return weather_data

        else:

            return None

    except Exception:

        return None