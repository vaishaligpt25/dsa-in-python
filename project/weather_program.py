# https://www.youtube.com/watch?v=SqvVm3QiQVk&t=1494s

import requests
from pprint import pprint

API_Key = "e0129df9e8e60df521cbd86f0e091a9c"
city = input("Enter a city: ")
base_url = "http://api.openweathermap.org./data/2.5/weather?appid="+API_Key+"&q="+city
weather_data = requests.get(base_url).json()
pprint(weather_data)