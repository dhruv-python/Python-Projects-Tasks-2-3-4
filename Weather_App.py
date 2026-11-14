"""Task 4: Basic OpenWeatherMap Weather App."""
import os
import requests

API_URL = "https://api.openweathermap.org/data/2.5/weather"

def main():
    print("\n=== Basic Weather App ===")
    city = input("Enter city name: ").strip()
    if not city:
        print("City name cannot be empty.")
        return

    api_key = os.getenv("OPENWEATHER_API_KEY", "").strip()
    if not api_key:
        api_key = input("Enter your OpenWeatherMap API key: ").strip()
    if not api_key:
        print("API key is missing.")
        return

    try:
        response = requests.get(
            API_URL,
            params={"q": city, "appid": api_key, "units": "metric"},
            timeout=10
        )
        if response.status_code == 404:
            print("City not found. Check the spelling.")
            return
        if response.status_code == 401:
            print("Invalid or inactive API key. Check your key.")
            return
        response.raise_for_status()
        data = response.json()

        temp_c = data["main"]["temp"]
        temp_f = temp_c * 9 / 5 + 32
        print(f"\n--- Weather in {data.get('name', city)} ---")
        print(f"Temperature: {temp_c:.1f} °C")
        print(f"Temperature: {temp_f:.1f} °F")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Condition: {data['weather'][0]['description'].capitalize()}")
        print(f"Wind speed: {data['wind']['speed']} m/s")

    except requests.exceptions.Timeout:
        print("Request timed out. Try again.")
    except requests.exceptions.ConnectionError:
        print("Network error. Check your internet connection.")
    except requests.exceptions.HTTPError as error:
        print(f"Weather service error: {error}")
    except (KeyError, IndexError, ValueError):
        print("Could not understand the weather response. Try again.")
    except requests.exceptions.RequestException as error:
        print(f"Request failed: {error}")

if __name__ == "__main__":
    main()
