# Teste Python Microservices
Por questão de simplicidade para rever o código nesse repositório tem dois micro
serviços.


## Variaveis e credenciais
As variáveis como urls, e token para a api do Open Weather
podem ser amazenada em variáveis de ambiente linux ou se preferir em um
arquivo chamado settings.ini que deve ficar fora do repositório
por questão de segurança. Essas são as variáveis que precisa ter ou em variavel de ambiente ou
no arquivo settings.ini

    
        url_microservice1 = http://127.0.0.1:3001/
        api_key_open_weather = api key do Open Weather
        url_open_weather = https://api.openweathermap.org/data/2.5/weather