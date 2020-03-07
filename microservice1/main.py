import uvicorn
from fastapi import FastAPI

from microservice1.base_model import BaseModelRegisterForecast
from microservice1.register_forecast import create_task

app = FastAPI()


@app.get("/")
def info_microservice():
    """Microservice1 - Responsável por expor API Rest para cadastrar previsão do tempo
    -Deve produzir uma mensagem para o broker requisitando a operação de Consulta de Previsão
    de Tempo.
    -Deve escutar a resposta do broker com a previsão de tempo e armazenar em um Banco de
    Dados"""

    return {"Microservice1": "Responsável por expor API Rest para cadastrar previsão do tempo"}


@app.post("/register_forecast", response_model=BaseModelRegisterForecast)
def register_weather(forecast: BaseModelRegisterForecast):
    """
        Para cadastrar um previsão do tempo é obrigatório informar o campo city, sendo os campos state e city opcionais
    """
    create_task(forecast)
    return forecast


if __name__ == '__main__':
    uvicorn.run(app, port=3001, log_level="info")
