import requests
import os

LAT = "47.497913"
LON = "19.040236"
API_KEY = os.environ.get("API_KEY")
URL = f"https://api.openweathermap.org/data/4.0/onecall/current?lat={LAT}&lon={LON}&appid={API_KEY}"

try:
    response = requests.get(url=URL)
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    print("HTTP error occurred:", e)
except requests.exceptions.RequestException as e:
    print("A request error occurred:", e)

