import pytest
from unittest.mock import MagicMock
import requests
from api_client import WeatherApiClient

def test_fetch_current_weather_success():
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "name": "Budapest",
        "main": {"temp": 22.5, "humidity": 55}
    }

    client = WeatherApiClient(url="https://api.fake-weather.com", api_key="fake_api_key")
    client.session.get = MagicMock(return_value=mock_response)

    result = client.fetch_current_weather("Budapest")

    assert result is not None
    assert result["name"] == "Budapest"
    assert result["main"]["temp"] == 22.5
    
    client.session.get.assert_called_once()

def test_fetch_current_weather_http_error():
    mock_response = MagicMock()
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Not Found")

    client = WeatherApiClient(url="https://api.fake-weather.com", api_key="fake_api_key")
    client.session.get = MagicMock(return_value=mock_response)

    result = client.fetch_current_weather("IsmeretlenVaros")

    assert result is None