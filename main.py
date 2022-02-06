import json
import requests

filepath = "api_key.json"

with open(filepath, "r") as f:
    data = json.load(f)
    API_KEY = (data['API_KEY'])

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter city: ")
state = input("Enter state: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city},{state}"
response = requests.get(request_url)

def to_f(K):
    return (K - 273.15) * 9 / 5 + 32

if response.status_code == 200:
    data = response.json()
    name = data['name']
    desc = data['weather'][0]['description']
    temp = data['main']['temp']
    temp_f = round(to_f(temp))
    feel = data['main']['feels_like']
    feel_f = round(to_f(feel))
    tmin = data['main']['temp_min']
    tmin_f = round(to_f(tmin))
    tmax = data['main']['temp_max']
    tmax_f = round(to_f(tmax))
    print(f"In {name}, it is currently {desc} and {temp_f} degrees Fahrenheit.")
    print(f"Real feel is about {feel_f} degrees and you can expect a high of {tmax_f} degrees")
    print(f"and low of {tmin_f} degrees over the course of the day.")
else:
    print("There was an error. Try again")





