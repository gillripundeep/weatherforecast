# Weather Forecast API

Weather Forcast is a sample implementation of `FASTAPI` framework.

## Technology Stack
```
Python 3.9.3
FastAPI
uvicorn
```
## How to Setup
- Create a Virtual Environment (Optional but recommended). It's good practice to create a virtual environment for your FastAPI project. This isolates your project's dependencies from the system-wide Python installation. You can create a virtual environment using the following commands:
    ```
    python -m venv .venv 
    source venv/bin/activate
    ```
- Create a config.cfg file and position it at the same directory level as main.py. In this configuration file, set up a default profile and include your [Openweather API Key](https://openweathermap.org/api) and [Geopify API Key](https://www.geoapify.com/get-started-with-maps-api). The configuration should resemble the following example:
    ```
    [default]
    open_weather_api_key = 7XXXXXXXXXXXXXXXXXXXXXXXXXXXf
    geoapify_api_key = 0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXd
    ```
- FastAPI uses ASGI servers to run your application. Uvicorn is a popular ASGI server that works well with FastAPI. Install them and other dependencies using pip:
    ```
    pip install -r requirements.txt
    ```
- Run Your FastAPI App with Uvicorn.
    ```
    uvicorn main:app --reload
    ```
- Open a web browser or a tool like `httpie` or `Postman` and visit [Local Server](http://127.0.0.1:8000/) to see your FastAPI app in action.

- FastAPI automatically generates interactive documentation for your API. Access it by visiting [Local Server Docs](http://127.0.0.1:8000/docs) in your web browser.

## API DOCS

![Alt text](weather_forecast_api.png?raw=true "Weather Forecast API")

