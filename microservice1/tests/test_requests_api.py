from unittest import TestCase

import requests
from decouple import config


class TestRegisterForecast(TestCase):
    def setUp(self) -> None:
        self.url_base = config('url_microservice1')

    def test_response_code(self):
        response = requests.get(self.url_base)
        self.assertEqual(200, response.status_code)

    def test_response(self):
        response = requests.get(self.url_base)
        payload = response.json()
        self.assertIsNotNone(payload.get('Microservice1'))

    def test_endpoint_register_forecast(self):
        url = f"{self.url_base}register_forecast"
        payload = {'city': 'Blumenau'}
        response = requests.post(url, json=payload)
        self.assertEqual(200, response.status_code)
        payload = response.json()
        self.assertEqual('Blumenau', payload['name'])


