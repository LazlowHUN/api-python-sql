from pydantic import BaseModel

class WeatherMeausrement(BaseModel):
    dt: str
    sunrise: int
    sunset: int
    temp: float
    feels_like: float
    pressure: int
    humidity: int
    dew_point: float
    uvi: float
    clouds: int
    visibility: int
    wind_speed: float
    wind_deg: int

class WeatherResponse(BaseModel):
    lat: float
    lon: float
    timezone: str
    timezone_offset: int
    data: WeatherMeausrement