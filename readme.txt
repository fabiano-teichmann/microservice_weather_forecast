# Teste Python Microservices
Essa aplicação eu escolhi utilizar as seguintes tecnologias, FastApi para a API do microservice1.
Eu a escolhi pela simplicidade e agilidade que ela entrega. Mas os pontos ao meu ver mais importante
é por ter uma excelente perfomace. Roda com o Uvicorn que é assícrono. Outro ponto positivo é que
ela entrega de maneira pronta uma documentação da api. Podendo até mesmo testar os endpoint.
Para a comunicação com o segundo microservice eu utilizei o Celery com o Redis como broker. Podendo
esse projeto estar em servidores separados. A requisições para o segundo microserviço é assícrona
sendo que o 2 microservice retorna pelo Redis o resultado da consulta da API. E o banco de dados
que escolhi para salvar é o MongoDB. Não ficou claro para mim se vocês esperam a API não espere
o retorno ou espere em todo caso deixei comentado uma parte do código que chama uma coroutine e a API
não espera uma resposta do 2 microservice.


## Instalação do projeto
Primeiramente baixe o repositório com o comando

    git clone https://github.com/fabiano-teichmann/microservice_weather_forecast.git

Crie uma virtualenv e a ative com os comandos abaixo:

    python -m venv venv
    source venv/bin/activate

Instale as bibliotecas necessárias entrando na pasta do projeto e rodando o comando:

    pip install -r requirements.txt

Para poder funcionar o projeto é necessário ter o Redis instalado, por questão de
simplicidade recomendo rodar o Redis no docker baixando uma imagem  e rodando

       docker pull redis
       docker run -d -p 6379:6379 redis



## Variáveis e credenciais
As variáveis como urls, e token para a api do Open Weather
podem ser armazenada em variáveis de ambiente linux ou se preferir em um
arquivo chamado settings.ini que deve ficar fora do repositório
por questão de segurança. Essas são as variáveis que precisa ter ou em variavel de ambiente ou
no arquivo settings.ini


        url_microservice1 = http://127.0.0.1:3001/
        api_key_open_weather = api key do Open Weather
        url_open_weather = https://api.openweathermap.org/data/2.5/weather
        backend_url = 'redis://localhost:6379/1'
        broker_url = 'redis://localhost:6379/0'

## Rodando o celery
Para rodar o celery execute o seguinte comando dentro da pasta do projeto:

    celery -A microservice1.handler_broker worker --loglevel=info

Sendo que para ambiente de produção é necessário utilizar o Supervisor ou o Systemctl
do Linux para  o processo sempre estar ativo.


## Rodando a API
A api do microservice 1 usa o Uvicorn que usa o protocolo AWSGI e para executá-lo
entre na pasta microservice1 e rode o comando abaixo:

    uvicorn main:app --reload


Para acessar a API entre na url

     http://127.0.0.1:8000/docs

Onde vai ser carregado a documentação com os endpoints disponíveis. E por essa url pode-se testar
a aplicação cadastrando uma previsão do tempo. E vendo o resultado da consulta.








