import requests

def get_weather(api_key, city):
    # Define the base URL of the OpenWeatherMap API
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    # Set the parameters for the API request
    params = {
        "q": city,            # City name
        "appid": api_key,     # Your OpenWeatherMap API key
        "units": "metric"     # Units for temperature (Celsius)
    }
    # Send a GET request to the API with the specified parameters
    response = requests.get(base_url, params=params)
    # Parse the JSON data from the API response
    data = response.json()

    # Check if the API response status code is 200 (OK)
    if response.status_code == 200:
        # Extract relevant weather information from the API response
        weather_info = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
        return weather_info
    else:
        # Print an error message if there's an issue with the API request
        print("Error fetching weather data:", data.get("message",
                                                       "Unknown error"))
        return None

# Define the main function
def main():
    # Replace "YOUR_API_KEY_HERE" with your actual OpenWeatherMap API key
    api_key = "bd5e378503939ddaee76f12ad7a97608"
    # Get user input for the city name
    city = input("Enter city name: ")
    # Call the get_weather function to fetch weather data
    weather_data = get_weather(api_key, city)

    # Check if weather data was fetched successfully
    if weather_data:
        # Print the weather information
        print(f"Weather in {weather_data['city']}:")
        print(f"Temperature: {weather_data['temperature']}°C")
        print(f"Description: {weather_data['description']}")

# Execute the main function when the script is run
if __name__ == "__main__":
    main()
