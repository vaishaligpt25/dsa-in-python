import json

from project.weather_program_2.openweathermap_accessor import OpenWeatherMapAccessor

from typing import Dict, Any


class WeatherGetter:

    open_weather_map_accessor: OpenWeatherMapAccessor

    def __init__(self):
        self.open_weather_map_accessor: OpenWeatherMapAccessor = OpenWeatherMapAccessor()

    def show_weather_for_city(self, city: str) -> None:
        weather_data: Dict[str, Any] = self.open_weather_map_accessor.get_weather_data_for_city(city=city)
        print(json.dumps(weather_data, indent=2))

    def show_weather_for_lat_long(self, lat: float, long: float) -> None:
        weather_data: Dict[str, Any] = self.open_weather_map_accessor.get_weather_data_for_lat_long(lat=lat, long=long)
        print(json.dumps(weather_data, indent=2))
