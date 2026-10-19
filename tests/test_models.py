import pytest
from pydantic import ValidationError
from models import WeatherResponse

def test_weather_model_with_valid_data():
    valid_data = {"city": {
                    "id": 2867714,
                    "name": "Munich",
                    "coord": {
                    "lat": 48.1374,
                    "lon": 11.5755
                    },
                    "country": "DE",
                    "population": 1260391,
                    "timezone": 3600,
                    "sunrise": 1647322046,
                    "sunset": 1647364681
                },
                "cod": 
                "200", 
                "cnt": 1, 
                "list":
                    [{
                    "dt": 1647345600,
                    "main": {
                        "temp": 284.83,
                        "feels_like": 283.59,
                        "temp_min": 284.83,
                        "temp_max": 285.69,
                        "pressure": 1013,
                        "sea_level": 1013,
                        "grnd_level": 964,
                        "humidity": 59,
                        "temp_kf": -0.86
                    },
                    "weather": [
                        {
                        "id": 804,
                        "main": "Clouds",
                        "description": "overcast clouds",
                        "icon": "04d"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 0.7,
                        "deg": 288,
                        "gust": 2.1
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "d"
                    },
                    "dt_txt": "2022-03-15 12:00:00"
                    }]}
    model = WeatherResponse(**valid_data)
    assert model.city.name == "Munich"
    assert model.list[0].main.temp == 284.83

def test_weather_model_with_invalid_data():
    invalid_data = {"city": "Budapest", "temperature": "not_a_number"}
    with pytest.raises(ValidationError):
        WeatherResponse(**invalid_data)