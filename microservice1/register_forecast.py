from microservice1.base_model import BaseModelRegisterForecast


def create_task(forecast: BaseModelRegisterForecast):
    query_forecast.delay(forecast)