from pydantic.main import BaseModel


class BaseModelRegisterForecast(BaseModel):
    city: str
    state: str = ''
    country: str = ''
