import os
from typing import Dict, Any

import requests

class OpenWeatherMapAccessor:

    API_KEY: str = os.getenv("API_KEY")
    API_BASE_URL: str = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather_data_for_city(self, city: str) -> Dict[str, Any]:
        params: Dict[str, str] = {
            "q": city,
            "appid": self.API_KEY
        }

        response: requests.models.Response = requests.get(self.API_BASE_URL, params=params)
        weather_data: Dict[str, Any] = response.json()

        return weather_data
