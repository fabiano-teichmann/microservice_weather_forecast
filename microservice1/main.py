import asyncio

import uvicorn

from fastapi import FastAPI

from microservice1.base_model import BaseModelRegisterForecast
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


@app.post("/register_forecast")
def register_weather(forecast: BaseModelRegisterForecast):
    """
        Para cadastrar um previsão do tempo é obrigatório informar o campo city, sendo os campos state e city opcionais
        é disparado uma task para o celery e de modo assicrono fica escudando esperando a resposta
    """
    task = create_task(forecast)
    loop.run_in_executor(None, listen_broker, task)
    return {'status_code': 'Previsão do tempo cadastrada com sucesso'}


if __name__ == '__main__':
    uvicorn.run(app, port=3001, log_level="info")
