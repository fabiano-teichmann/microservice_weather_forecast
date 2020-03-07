import time

from celery import Celery

from microservice1.base_model import BaseModelRegisterForecast
from microservice2.main import get_forecast_weather

BACKEND_URL = 'redis://localhost:6379/1'
BROKER_URL = 'redis://localhost:6379/0'

app = Celery('tasks', broker=BROKER_URL, backend=BACKEND_URL)

# CELERY_RESULT_BACKEND = "redis"


def create_task(forecast: BaseModelRegisterForecast):

    task = get_forecast_weather.delay(forecast.dict())
    return task


def listen_broker(task):

    ready = task.ready()
    while ready is False:
        if task.ready():
            return task.get(timeout=1)

        ready = task.ready()
