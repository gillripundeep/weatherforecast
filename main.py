"""
WEATHER FORECAST

Weather Forcast is a sample implementation using
FastAPI framework. API are written to provide weather
forecast for the inputted city or in general.
"""


import logging
import datetime

from fastapi import FastAPI, HTTPException

from src import Helper
from src import CityData
from src import open_api_docs

app = FastAPI()

app.openapi_schema = open_api_docs

current_time = datetime.datetime.now().strftime("%Y%m%d")
logfilename = f"WF_{current_time}.log"
logging.basicConfig(filename=logfilename,
                    filemode='w',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)
helper = Helper(logging)

@app.get("/")
def read_root():
    "Weather Forecast API Metadata"
    return {
        "name": "Weather Forecast API",
        "version": "0.1.0",
        "description": "This is a sample API for demonstration purposes.",
        "contact": {
            "Author": "Ripundeep Singh Gill",
            "email": "ripundeep.gill@gmail.com"
            }
        }

@app.post("/weatherforecast", response_model=dict)
def weather_forecast(data: CityData):
    """Weather Forecast POST API"""
    try:
        # Retrieve latitude and longitude data
        city_data = helper.get_city_long_lat(data.city)
        # Get weather forecast using the retrieved coordinates
        weather_data = helper.get_weather_forecast(
            lon=city_data["longitude"], lat=city_data["latitude"])

        return {"response": weather_data}
    except HTTPException as err:
        return err
