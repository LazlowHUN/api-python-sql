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
            "sunrise": day_item.sunrise,
            "sunset": day_item.sunset,
            "temp_day": day_item.temp.day,
            "temp_min": day_item.temp.min,
            "temp_max": day_item.temp.max,
            "pressure": day_item.pressure,
            "humidity": day_item.humidity,
            "wind_speed": day_item.speed,
            "clouds": day_item.clouds,
            "rain": day_item.rain
        }
        processed_records.append(record)

    return processed_records