from pydantic import BaseModel
from typing import List, Optional

class TempInfo(BaseModel):
    day: float
    min: float
    max: float
    night: float
    eve: float
    morn: float

class FeelsLikeInfo(BaseModel):
    day: float
    night: float
    eve: float
    morn: float

class CityInfo(BaseModel):
    id: int
    name: str
    country: str
    population: int

class WeatherMeausrement(BaseModel):
    dt: str
    sunrise: int
    sunset: int
    temp: TempInfo
    feels_like: FeelsLikeInfo
    pressure: int
    humidity: int
    speed: float
    deg: int
    gust: Optional[float] = None
    clouds: int
    pop: float
    rain: Optional[float] = 0.0

class WeatherResponse(BaseModel):
    city: CityInfo
    cod: str
    cnt: int
    list: List[WeatherMeausrement]