import json

from project.weather_program_2.openweathermap_accessor import OpenWeatherMapAccessor

from typing import Dict, Any


class WeatherGetter:

    open_weather_map_accessor: OpenWeatherMapAccessor

    def __init__(self):
        self.open_weather_map_accessor: OpenWeatherMapAccessor = OpenWeatherMapAccessor()

    def show_weather_for_city(self, city: str) -> None:
        weather_data: Dict[str, Any] = self.open_weather_map_accessor.get_weather_data_for_city(city=city)
        print(json.dumps(weather_data, indent=4))

if __name__ == "__main__":
    weather_getter: WeatherGetter = WeatherGetter()

    city: str = input("Enter a city: ")
    weather_getter.show_weather_for_city(city=city)
