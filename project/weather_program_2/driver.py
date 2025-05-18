from project.weather_program_2.weather_getter import WeatherGetter

CHOICE_GET_WEATHER_FOR_CITY: int = 1
CHOICE_GET_WEATHER_FOR_LAT_LONG: int = 2
CHOICE_EXIT: int = 3

# to run this program in IntelliJ / PyCharm, we need to 'Edit Configurations' and set the "API_KEY" environment variable

def get_choice() -> int:
    print("==============================")
    print("==============================")
    print("Welcome to the weather program!")
    print("1. Get weather for city")
    print("2. Get weather for lat/long")
    print("3. Exit")
    print("..............................")
    choice: int = int(input("Enter your choice: "))
    print("..............................")
    return choice

def get_weather_for_city(weather_getter: WeatherGetter) -> None:
    city: str = input("Enter a city: ")
    print("..............................")
    weather_getter.show_weather_for_city(city=city)

def get_weather_for_lat_long(weather_getter: WeatherGetter) -> None:
    lat: float = float(input("Enter latitude: "))
    long: float = float(input("Enter longitude: "))
    print("..............................")
    weather_getter.show_weather_for_lat_long(lat=lat, long=long)

if __name__ == "__main__":
    weather_getter: WeatherGetter = WeatherGetter()

    choice: int = get_choice()
    while choice != CHOICE_EXIT:
        if choice == CHOICE_GET_WEATHER_FOR_CITY:
            get_weather_for_city(weather_getter)
        elif choice == CHOICE_GET_WEATHER_FOR_LAT_LONG:
            get_weather_for_lat_long(weather_getter)
        else:
            print("Invalid choice")

        choice: int = get_choice()
