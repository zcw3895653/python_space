from pydantic import BaseModel


class Tianqi(BaseModel):
    tianqi_id:str
    city: str
    cityid: str
    temp:float
    weather: str

