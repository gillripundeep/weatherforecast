import requests
from logging import Logger

from constants import (
    OPEN_WEATHER_API, GEOPIFY_URL, OPEN_WEATHER_API_KEY, GEOPIFY_API_KEY
)

class Helper:
    def __init__(self, logging:Logger) -> None:
        self.logging = logging

    def get_city_long_lat(self, city):
        self.logging.info(f"Fetching longitude and latitude for given city")
        geopify_url = GEOPIFY_URL.format(city=city, apikey=GEOPIFY_API_KEY)
        response = requests.get(geopify_url)
        # Check the response status code
        if response.status_code == 200:
            # Parse the JSON data from the response
            data = response.json()
            # Extract the first result from the data
            result = data["features"][0]
            # Extract the latitude and longitude of the result
            latitude = result["geometry"]["coordinates"][1]
            longitude = result["geometry"]["coordinates"][0]
            return{"latitude": latitude, "longitude": longitude}
        else:
            self.logging.error(f"Request failed with status code {response.status_code}")
            raise Exception(f"Request failed with status code {response.status_code}")
    
    def get_weather_forecast(self, long, lat):
        self.logging.info(f"Fetching weather forecast data for given longitude and latitude")
        url = OPEN_WEATHER_API.format(lat=lat,lon=long,APIkey=OPEN_WEATHER_API_KEY)
        response = requests.get(url)
        print(url)
        # Check the response status code
        if response.status_code == 200:
            result = response.json()
            print(result)
            return result
        else:
            self.logging.error(f"Request failed with status code {response.status_code}")
            raise Exception(f"Request failed with status code {response.status_code}")