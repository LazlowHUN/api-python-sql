import logging
import psycopg2
from psycopg2.extras import execute_values
from transformer import process_weather_response

logger = logging.getLogger(__name__)

class DbManager():
    def __init__(self, connection_string: str):
        self.conn_str = connection_string

    def upsert_data(self, data: list[dict]):
        if not data:
            raise ValueError("There are no rows to insert")

        columns = [
            "city_id", "dt", "temp", "feels_like", "pressure",
            "humidity", "wind_speed", "dt_txt"
        ]

        values = [tuple(item[col] for col in columns) for item in data]

        query = f"""
            INSERT INTO weather_measurements({', '.join(columns)})
            VALUES %s
            ON CONFLICT (city_id, dt)
            DO UPDATE SET
                temp = EXCLUDED.temp,
                feels_like = EXCLUDED.feels_like,
                pressure = EXCLUDED.pressure,
                humidity = EXCLUDED.humidity,
                wind_speed = EXCLUDED.wind_speed,
                dt_txt = EXCLUDED.dt_txt,
                created_at = EXCLUDED.created_at;
        """

        with psycopg2.connect(self.conn_str) as conn:
            with conn.cursor() as curs:
                execute_values(query, values)
                conn.commit()
