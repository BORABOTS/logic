import requests
API_KEY = "6067aea698b96aea780ad2233fd44cde"

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)

        # Check status
        if response.status_code != 200:
            print("Error:", response.status_code)
            print(response.text)
            return

        data = response.json()

        # Extract data
        city_name = data["name"]
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]

        print(f"City: {city_name}")
        print(f"Temperature: {temp}°C")
        print(f"Weather: {weather}")

    except Exception as e:
        print("Error occurred:", e)


# Test
city=input("get your city: ")
get_weather("city")