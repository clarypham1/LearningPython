#1)
import requests

def get_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    data = response.json()
    print(data["value"])

get_chuck_norris_joke()

#2)
import requests

def get_weather():
    city = input("Enter municipality name: ")
    api_key = "YOUR_API_KEY_HERE"

    url = (
        f"https://api.openweathermap.org/data/2.5/weather?q={city}"
        f"&appid={api_key}"
    )

    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        print("City not found.")
        return

    description = data["weather"][0]["description"]
    kelvin_temp = data["main"]["temp"]
    celsius_temp = kelvin_temp - 273.15

    print(f"Weather condition: {description}")
    print(f"Temperature: {celsius_temp:.2f} °C")

get_weather()
