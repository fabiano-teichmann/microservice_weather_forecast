from celery import Celery

from microservice1.base_model import BaseModelRegisterForecast
from microservice2.api_forecast_weather import ApiForecastWeather

BROKER_URL = 'redis://localhost:6379/0'
BACKEND_URL = 'redis://localhost:6379/1'
app = Celery('tasks', broker=BROKER_URL, backend=BACKEND_URL)

@app.task
def get_forecast_weather(forecast: dict):
    data = BaseModelRegisterForecast(**forecast)
    return ApiForecastWeather(data).get_forecast()




