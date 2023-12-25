import requests

def get_weather(city):    
    api_key = 'cant share it '
    base_url = 'site is stromglass.io'

    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Units for temperature (metric for Celsius)
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        weather = {
            'description': data['weather'][0]['description'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity']
            # Add more data fields as needed
        }
        return weather
    else:
        return None

def main():
    city = input("Enter city name: ")
    weather = get_weather(city)

    if weather:
        print(f"Weather in {city}:")
        print(f"Description: {weather['description']}")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Humidity: {weather['humidity']}%")
        # Display more weather information
    else:
        print("Weather data not available.")

# Start the app
main()