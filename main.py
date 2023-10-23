"""
WEATHER FORECAST

Weather Forcast is a sample implementation using
FastAPI framework. API are written to provide weather
forecast for the inputted city or in general.
"""


import logging
import datetime

from fastapi import FastAPI

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

@app.post("/weatherforecast")
def weatherforecast(data: CityData):
    """Weather Forecast GET API"""
    try:
        get_lat_long_data = helper.get_city_long_lat(data.city)
        get_weather_data = helper.get_weather_forecast(
            long=get_lat_long_data["longitude"],
            lat=get_lat_long_data["latitude"]
            )
        return {"response": get_weather_data}
    except Exception as errmsg:
        return {"response":errmsg}
