from pydantic import BaseModel
from typing import List, Optional

class MainInfo(BaseModel):
    temp: float
    feels_like: float
    pressure: int
    humidity: int

class WindInfo(BaseModel):
    speed: float
    deg: int

class CityInfo(BaseModel):
    id: int
    name: str
    country: str
    population: int

class ForecastItem(BaseModel):
    dt: int
    main: MainInfo
    wind: WindInfo
    dt_txt: str

class WeatherResponse(BaseModel):
    city: CityInfo
    cod: str
    cnt: int
    list: List[ForecastItem]