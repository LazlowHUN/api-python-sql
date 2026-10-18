import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
import logging

logger = logging.getLogger(__name__)

class WeatherApiClient:
    def __init__(self, url: str, api_key: str, lat: str, lon: str):
        self.url = url
        self.api_key = api_key
        self.lat = lat
        self.lon = lon
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

    def fetch_current_weather(self):
        try:
            params = {"lat": self.lat, "lon": self.lon, "appid": self.api_key}
            response = self.session.get(self.url, params=params, timeout=10)
            response.raise_for_status()

            logger.info("Data fetched")
            return response.json()
        
        except requests.exceptions.HTTPError as e:
            logger.exception("HTTP error occurred")
        except requests.exceptions.RequestException as e:
            logger.exception("A request error occurred")