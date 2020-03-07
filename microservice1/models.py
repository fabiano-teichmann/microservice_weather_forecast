from pymongo import MongoClient


def save_db(forecast: dict):
    client = MongoClient('localhost', 27017)
    db = client['microservice1']
    collection = db['forecast_weather']
    collection.insert_one(forecast)


