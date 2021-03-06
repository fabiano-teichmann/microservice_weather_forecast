import asyncio

from fastapi import FastAPI

from microservice1.base_model import BaseModelRegisterForecast, BaseForecast
from microservice1.handler_broker import listen_broker, create_task

app = FastAPI()
loop = asyncio.new_event_loop()


@app.get("/")
def info_microservice():
    """Microservice1 - Responsável por expor API Rest para cadastrar previsão do tempo
    -Deve produzir uma mensagem para o broker requisitando a operação de Consulta de Previsão
    de Tempo.
    -Deve escutar a resposta do broker com a previsão de tempo e armazenar em um Banco de
    Dados"""

    return {"Microservice1": "Responsável por expor API Rest para cadastrar previsão do tempo"}


@app.post("/register_forecast", response_model=BaseForecast)
def register_weather(forecast: BaseModelRegisterForecast):
    """
        Para cadastrar um previsão do tempo é obrigatório informar o campo city, sendo os campos state e city opcionais

    """
    task = create_task(forecast)
    response = listen_broker(task)
    response = BaseForecast(**response)
    return response
    # loop.run_in_executor(None, listen_broker, task)
    # return {'status_code': 'Previsão do tempo cadastrada com sucesso'}



