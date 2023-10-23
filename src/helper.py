"""
The 'Helper' module comprises functions designed
to streamline the code for an API, offering a variety
of methods to deliver the desired results more efficiently.
"""
from logging import Logger

import requests

from constants import (
    OPEN_WEATHER_API, GEOPIFY_URL, OPEN_WEATHER_API_KEY, GEOPIFY_API_KEY
)


class Helper:
    """Class Helper"""
    def __init__(self, logging:Logger) -> None:
        """Initialization"""
        self.logging = logging

    def get_city_long_lat(self, city):
        """Fetch the Longitude and Latitude of Given City"""
        try:
            self.logging.info(f"Fetching longitude and latitude for the city: {city}")
            geopify_url = GEOPIFY_URL.format(city=city, apikey=GEOPIFY_API_KEY)

            response = requests.get(geopify_url, timeout=5)

            if response.status_code == 200:
                data = response.json()
                result = data.get("features", [{}])[0]  # Use .get() to handle missing keys
                latitude = result.get("geometry", {}).get("coordinates", [])[1]
                longitude = result.get("geometry", {}).get("coordinates", [])[0]

                if latitude is not None and longitude is not None:
                    return {"latitude": latitude, "longitude": longitude}
                raise Exception("Latitude or longitude data is missing in the response")

            self.logging.error(f"Request failed with status code {response.status_code}")
            raise Exception(f"Request failed with status code {response.status_code}")

        except requests.exceptions.RequestException as err:
            self.logging.error(f"Request failed with an exception: {str(err)}")
            raise Exception(f"Request failed with an exception: {str(err)}") from err

    def get_weather_forecast(self, lon, lat):
        """Fetch the Weather Data For Given Longitude and Latitude"""
        # Log an informative message
        self.logging.info(f"Fetching weather forecast data for latitude {lat} and longitude {lon}")

        # Create the API URL with parameters
        url = OPEN_WEATHER_API.format(lat=lat, lon=lon, APIkey=OPEN_WEATHER_API_KEY)

        try:
            # Make the GET request with a timeout of 5 seconds
            response = requests.get(url, timeout=5)
            response.raise_for_status()  # Raise an exception for non-2xx status codes

            # Check the response status code
            if response.status_code == 200:
                result = response.json()
                return result
            self.logging.error(f"Request failed with status code {response.status_code}")
            raise Exception(f"Request failed with status code {response.status_code}")

        except requests.RequestException as err:
            self.logging.error(f"Request to the weather API failed: {str(err)}")
            raise Exception(f"Request to the weather API failed: {str(err)}") from err
