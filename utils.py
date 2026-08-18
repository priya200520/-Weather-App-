import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")


# Get coordinates of city
def get_coordinates(city):

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
        return None

    return {
        "lat": geo_data[0]["lat"],
        "lon": geo_data[0]["lon"],
        "city": geo_data[0]["name"]
    }


# Get current weather
def get_weather(city):

    if not API_KEY:
        return {
            "error": "API key not found. Check your .env file."
        }

    try:

        location = get_coordinates(city)

        if not location:
            return {
                "error": "City not found"
            }

        weather_url = (
            "https://api.openweathermap.org/data/2.5/weather"
        )

        weather_params = {
            "lat": location["lat"],
            "lon": location["lon"],
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
            "city": location["city"],
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


# Get 5-day forecast
def get_forecast(city):

    if not API_KEY:
        return {
            "error": "API key not found. Check your .env file."
        }

    try:

        location = get_coordinates(city)

        if not location:
            return {
                "error": "City not found"
            }

        forecast_url = (
            "https://api.openweathermap.org/data/2.5/forecast"
        )

        forecast_params = {
            "lat": location["lat"],
            "lon": location["lon"],
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(
            forecast_url,
            params=forecast_params,
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

        forecast_data = []

        for item in data["list"]:

            forecast_data.append({
                "date": item["dt_txt"],
                "temperature": item["main"]["temp"],
                "weather": item["weather"][0]["description"],
                "humidity": item["main"]["humidity"],
                "wind_speed": item["wind"]["speed"]
            })

        return forecast_data

    except requests.exceptions.RequestException as e:
        return {
            "error": f"Network error: {str(e)}"
        }

    except Exception as e:
        return {
            "error": str(e)
        }
    # 5-day forecast feature added