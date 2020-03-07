import requests
from decouple import config
from requests import ReadTimeout, Response

from microservice1.base_model import BaseModelRegisterForecast


class ApiForecastWeather:
    def __init__(self, forecast: BaseModelRegisterForecast):
        self.url_base = config('url_open_weather')
        self.token = config('api_key_open_weather')
        self.forecast = forecast

    def url_request(self):
        """Mount url request join url base with query and token auth"""
        url = f"{self.url_base}?q="
        request = self.query_by_city_state_country(url)
        return f"{request}&appid={self.token}"

    def query_by_city_state_country(self, url: str) -> str:

        if self.forecast.state and self.forecast.country:
            return f"{url}{self.forecast.city}, {self.forecast.state}, {self.forecast.country}"
        else:
            return self.query_by_city_state(url)

    def query_by_city_state(self, url: str):
        if self.forecast.state:
            return f"{url}{self.forecast.city}, {self.forecast.state}"
        else:
            return self.query_by_city(url)

    def query_by_city(self, url: str):
        return f"{url}{self.forecast.city}"

    @staticmethod
    def send_request(url: str):
        try:
            response = requests.get(url, timeout=20)
        except ReadTimeout:
            return "A api demorou muito para responder"
        except ConnectionError:
            return "Erro conexão"

        return response

    def get_forecast(self):
        url = self.url_request()
        response = self.send_request(url)
        if isinstance(response, Response) and response.status_code == 200:
            return response.json()
        else:
            return response
