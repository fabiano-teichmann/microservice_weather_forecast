from unittest import TestCase

from microservice2.api_forecast_weather import ApiForecastWeather
from microservice1.base_model import BaseModelRegisterForecast


class TestApi(TestCase):
    def test_get_forecast(self):
        data = {'city': 'Blumenau'}
        forecast = BaseModelRegisterForecast(**data)
        forecast = ApiForecastWeather(forecast).get_forecast()
        self.assertEqual(forecast['name'], 'Blumenau')






