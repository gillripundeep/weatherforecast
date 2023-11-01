"""
Constants
"""
import configparser

CONFIG = configparser.ConfigParser()
CONFIG.read('config.cfg')

OPEN_WEATHER_API_KEY = CONFIG["default"]["open_weather_api_key"]
GEOPIFY_API_KEY = CONFIG["default"]["geoapify_api_key"]

OPEN_WEATHER_API_STR1 = "https://api.openweathermap.org/data/2.5/weather?"
OPEN_WEATHER_API_STR2 = "lat={lat}&lon={lon}&appid={APIkey}"
OPEN_WEATHER_API = f"{OPEN_WEATHER_API_STR1}{OPEN_WEATHER_API_STR2}"
GEOPIFY_URL = "https://api.geoapify.com/v1/geocode/search?city={city}&limit=1&apiKey={apikey}"
