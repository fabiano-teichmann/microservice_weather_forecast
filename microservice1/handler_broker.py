from celery import Celery

from microservice1.base_model import BaseModelRegisterForecast

from microservice2.main import get_forecast_weather

BACKEND_URL = 'redis://localhost:6379/1'
BROKER_URL = 'redis://localhost:6379/0'

app = Celery('tasks', broker=BROKER_URL, backend=BACKEND_URL)


def create_task(forecast: BaseModelRegisterForecast):
    task = app.send_task('microservice2.main.get_forecast_weather', (forecast.dict(),))
    return task


def listen_broker(task):

    ready = False
    while ready is False:
        ready = task.ready()
        if ready:

            return task.get(timeout=1)
