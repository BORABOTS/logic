import requests
def get_weather(city_name):
    # It's best to use f-strings or .format() for URLs
    api_key = "6067eaa0b9b56ab1760bd2233f044cde"
    city_name=input("Enter city:").strip().replace("","%20")
    url = f"https://openweathermap.org{city_name}&appid={api_key}&units=metric"

    try:
        # Set a timeout of 5 seconds to avoid waiting forever
        response = requests.get(url, timeout=5)
        
        # Check if the city was found (404 error)
        if response.status_code == 404:
            return f"Error: City '{city_name}' not found."
            
        # Raise an exception for other types of errors (e.g., 401, 500)
        response.raise_for_status()
        
        data = response.json()
        
        # Standard extraction with safe .get() method
        main = data.get('main', {})
        weather = data.get('weather', [{}])[0]
        
        return {
            "temp": main.get('temp'),
            "feels_like": main.get('feels_like'),
            "humidity": main.get('humidity'),
            "desc": weather.get('description')
        }
    except requests.exceptions.ConnectionError:
        return "Error: Could not connect to the internet. Please check your connection."
    except requests.exceptions.Timeout:
        return "Error: The request timed out. The server took too long to respond."
    except requests.exceptions.RequestException as e:
        return f"An unexpected error occurred: {e}"

# Running the app
city = input("Enter the name of the city: ")
result = get_weather(city)

if isinstance(result, dict):
    print(f"\nWeather in {city}:")
    print(f"Condition: {result['desc']}")
    print(f"Temperature: {result['temp']}°C (Feels like: {result['feels_like']}°C)")
    print(f"Humidity: {result['humidity']}%")
else:
    print(result)
