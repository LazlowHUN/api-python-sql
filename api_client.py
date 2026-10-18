import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
import logging

logger = logging.getLogger(__name__)

class WeatherApiClient:
    def __init__(self, url: str, api_key: str):
        self.url = url
        self.api_key = api_key
        self.session = self._get_session()

    def _get_session(self):
        session = requests.Session()

        retries = Retry(total=5,
                        backoff_factor=2,
                        status_forcelist=[ 500, 502, 503, 504 ],
                        raise_on_status=False)

        adapter = HTTPAdapter(max_retries=retries)
        session.mount('http://', adapter)
        session.mount('https://', adapter)

        return session

    def get_coordinates(self, city):
        endpoint = "http://api.openweathermap.org/geo/1.0/direct"
        params = {"q": city, "limit": 1, "appid": self.api_key}

        try:
            response = self.session.get(endpoint, params=params, timeout=10)
            response.raise_for_status()

            logger.info("Coordinates are fetched")
            data = response.json()
        
        except requests.exceptions.HTTPError as e:
            logger.exception("HTTP error occurred")
        except requests.exceptions.RequestException as e:
            logger.exception("A request error occurred")

        if not data:
            raise ValueError(f"There are no coordinates for this city: {city}")

        lat = data[0]["lat"]
        lon = data[0]["lon"]
        
        return lat, lon

    def fetch_1_min_weather(self, city: str):
        lat, lon = self.get_coordinates(city)
        params = {"lat": lat, "lon": lon, "appid": self.api_key, "units": "metric"}
        endpoint = f"{self.url}/onecall/timeline/1min"
        
        try:
            response = self.session.get(endpoint, params=params, timeout=10)
            response.raise_for_status()

            logger.info("Data fetched")
            return response.json()
        
        except requests.exceptions.HTTPError as e:
            logger.exception("HTTP error occurred")
        except requests.exceptions.RequestException as e:
            logger.exception("A request error occurred")