# https://www.youtube.com/watch?v=SqvVm3QiQVk&t=1494s
import os

from typing import Dict, Any

import requests
from pprint import pprint

api_key: str = os.getenv("API_KEY")
city: str = input("Enter a city: ")

# base_url: str = "http://api.openweathermap.org./data/2.5/weather?appid="+API_Key+"&q="+city
# weather_data = requests.get(base_url).json()

base_url: str = "http://api.openweathermap.org/data/2.5/weather"
params: Dict[str, str] = {
    "q": city,
    "appid": api_key
}

response: requests.models.Response = requests.get(base_url, params=params)
weather_data: Dict[str, Any] = response.json()

pprint(weather_data)
