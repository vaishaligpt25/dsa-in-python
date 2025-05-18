import os
from typing import Dict, Any

import requests

class OpenWeatherMapAccessor:

    API_KEY: str = os.getenv("API_KEY")
    CURRENT_WEATHER_API_BASE_URL: str = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather_data_for_city(self, city: str) -> Dict[str, Any]:
        params: Dict[str, str] = {
            "q": city,
            "appid": self.API_KEY
        }
        return self._get_weather_data(params)

    def get_weather_data_for_lat_long(self, lat: float, long: float) -> Dict[str, Any]:
        params: Dict[str, str] = {
            "lat": str(lat),
            "lon": str(long),
            "appid": self.API_KEY
        }
        return self._get_weather_data(params)

    def _get_weather_data(self, params: Dict[str, str]) -> Dict[str, Any]:
        response: requests.models.Response = requests.get(self.CURRENT_WEATHER_API_BASE_URL, params=params)
        weather_data: Dict[str, Any] = response.json()
        return weather_data
