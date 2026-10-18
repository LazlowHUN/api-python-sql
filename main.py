from api_client import WeatherApiClient
from db_manager import DbManager
from transformer import process_weather_response
import os
import logging

logger = logging.getLogger(__name__)

def run_pipeline():
    client = WeatherApiClient(url="api.openweathermap.org/data/2.5/forecast/daily", api_key=os.environ.get("API_KEY"))
    db = DbManager(os.environ.get("CONN_STR"))

    cities = ["Budapest", "Rome"]

    all_records = []

    for city in cities:
        try:
            raw_data = client.fetch_current_weather(city)

            record = process_weather_response(raw_data)

            all_records.append(record)
        except Exception as e:
            logger.exception("Something went wrong")

    if all_records:
        db.upsert_data(all_records)
        logger.info("Rows inserted")

if __name__ == "__main__":
    run_pipeline()