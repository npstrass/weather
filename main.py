import json
import requests
import pytz

filepath = "api_key.json"

with open(filepath, "r") as f:
    data = json.load(f)
    API_KEY = (data['API_KEY'])

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
    current_temp = data['main']['temp']
    current_temp_f = round(to_f(current_temp))
    real_feel = data['main']['feels_like']
    real_feel_f = round(to_f(real_feel))
    temp_min = data['main']['temp_min']
    temp_min_f = round(to_f(temp_min))
    temp_max = data['main']['temp_max']
    temp_max_f = round(to_f(temp_max))

    print('')
    print('')
    print('---')
    print(f"Today is {date} and currently {time}.")
    print(f"In {city_name}, we are seeing {weather_description} with temperatures of {current_temp_f} degrees.")
    print(f"Difference between actual and real feel is {current_temp_f - real_feel_f} with real feel at {real_feel_f} degrees.")
    print(f"Expect a high of {temp_max_f} and low of {temp_min_f} over the course of the day.")
else:
    print("There was an error. Try again")