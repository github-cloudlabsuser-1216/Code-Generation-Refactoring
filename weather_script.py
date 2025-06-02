import requests
import os

def fetch_weather(api_key, city):
    url = f"https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    try:
        weather = fetch_weather("9a18fe230cbafc30cbbf8a6d8c858f4f", "London")
        print(f"Weather in London: {weather['weather'][0]['description'].capitalize()}, Temperature: {weather['main']['temp']}°C")
    except requests.HTTPError as e:
        print(f"Failed to fetch weather data: {e}")