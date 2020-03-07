from bson import ObjectId
from pydantic.main import BaseModel


class BaseModelRegisterForecast(BaseModel):
    city: str
    state: str = ''
    country: str = ''


class ObjectIdStr(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, ObjectId):
            raise ValueError("Not a valid ObjectId")
        return str(v)


class BaseForecast(BaseModel):

    coord: dict
    weather: list
    base: str
    main: dict
    visibility: int
    wind: dict
    dt: int
    sys: dict
    timezone: int
    id: int
    name: str

