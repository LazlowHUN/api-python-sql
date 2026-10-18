import logging
from models import WeatherResponse

logger = logging.getLogger(__name__)

def process_weather_response(raw_json: dict) -> list[dict]:
    validated_response = WeatherResponse.model_validate(raw_json)

    city_id = validated_response.city.id
    processed_records = []

    for day_item in validated_response.list:
        record = {
            "city_id": city_id,
            "dt": day_item.dt,
            "temp": day_item.main.temp,
            "feels_like": day_item.main.feels_like,
            "pressure": day_item.main.pressure,
            "humidity": day_item.main.humidity,
            "wind_speed": day_item.wind.speed,
            "dt_txt": day_item.dt_txt
        }
        processed_records.append(record)

    return processed_records