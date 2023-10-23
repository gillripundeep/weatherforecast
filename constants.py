"""
Constants
"""
import configparser

CONFIG = configparser.ConfigParser()
CONFIG.read('config.cfg')

OPEN_WEATHER_API_KEY = CONFIG["default"]["open_weather_api_key"]
GEOPIFY_API_KEY = CONFIG["default"]["geoapify_api_key"]

OPEN_WEATHER_API = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={APIkey}"
GEOPIFY_URL = "https://api.geoapify.com/v1/geocode/search?text={city}&limit=1&apiKey={apikey}"
