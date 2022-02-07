import json
import requests
import pytz

filepath = "api_key.json"

with open(filepath, "r") as f:
    file_data = json.load(f)
    API_KEY = (file_data['API_KEY'])

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter city: ")
state = input("Enter state: ")
from datetime import datetime
request_url = f"{BASE_URL}?appid={API_KEY}&q={city},{state}"
response = requests.get(request_url)


def to_f(K):
    return (K - 273.15) * 9 / 5 + 32

if response.status_code == 200:
    data = response.json()
    current_timezone = pytz.FixedOffset(int(data['timezone'] / 60))
    local_time = datetime.now(current_timezone)
    date = local_time.strftime('%m-%d-%Y')
    time = local_time.strftime('%H:%M')
    city_name = data['name']
    weather_description = data['weather'][0]['description']
    current_temp = round(to_f(data['main']['temp']))
    real_feel = round(to_f(data['main']['feels_like']))
    temp_min = round(to_f(data['main']['temp_min']))
    temp_max = round(to_f(data['main']['temp_max']))
    print('---')
    print(f"Today is {date} and currently {time}.")
    print(f"In {city_name}, we are seeing {weather_description} with temperatures of {current_temp} degrees.")
    print(f"Difference between actual and real feel is {current_temp - real_feel} with real feel at {real_feel} degrees.")
    print(f"Expect a high of {temp_max} and low of {temp_min} over the course of the day.")
    print('---')
else:
    print("There was an error. Try again")