import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if data.get('cod') != 200:
        print("❌ City not found or API error:", data.get('message'))
        return

    weather = data['weather'][0]['description']
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    print(f"\n🌍 Weather in {city.title()}:")
    print(f"🌡️ Temperature: {temp}°C (Feels like {feels_like}°C)")
    print(f"💧 Humidity: {humidity}%")
    print(f"🌬️ Wind Speed: {wind_speed} m/s")
    print(f"🌈 Description: {weather.capitalize()}")

# Replace with your actual API key
api_key = 'b5cb65305b8c9bae3da00d7769093c0d'
city = input("Enter city name: ")
get_weather(city, api_key)