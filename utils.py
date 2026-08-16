import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")


def get_weather(city):

    if not API_KEY:
        return {
            "error": "API key not found. Check your .env file."
        }

    try:

        # Step 1: Find city coordinates using Geocoding API
        geo_url = "https://api.openweathermap.org/geo/1.0/direct"

        geo_params = {
            "q": f"{city},IN",
            "limit": 1,
            "appid": API_KEY
        }

        geo_response = requests.get(
            geo_url,
            params=geo_params,
            timeout=10
        )

        geo_data = geo_response.json()

        if not geo_data:
            return {
                "error": "City not found"
            }

        latitude = geo_data[0]["lat"]
        longitude = geo_data[0]["lon"]

        city_name = geo_data[0]["name"]


        # Step 2: Get weather using coordinates
        weather_url = (
            "https://api.openweathermap.org/data/2.5/weather"
        )

        weather_params = {
            "lat": latitude,
            "lon": longitude,
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(
            weather_url,
            params=weather_params,
            timeout=10
        )

        data = response.json()

        if response.status_code != 200:
            return {
                "error": data.get(
                    "message",
                    f"API Error: {response.status_code}"
                )
            }

        return {
            "city": city_name,
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "weather": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"],
            "visibility": data.get("visibility", 0) / 1000
        }

    except requests.exceptions.RequestException as e:
        return {
            "error": f"Network error: {str(e)}"
        }

    except Exception as e:
        return {
            "error": str(e)
        }