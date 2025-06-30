import argparse
import requests
import sys

parser = argparse.ArgumentParser(description="Weather forecast by city")
parser.add_argument("city", help="City name (e.g. Yerevan)")
parser.add_argument("-f", "--field", help="Show only a specific weather field")
parser.add_argument("--options", action="store_true", help="Show available weather fields")

AVAILABLE_FIELDS = {
    "temperature": lambda data: f"{data['current_condition'][0]['temp_C']} °C",
    "feels_like": lambda data: f"{data['current_condition'][0]['FeelsLikeC']} °C",
    "humidity": lambda data: f"{data['current_condition'][0]['humidity']}%",
    "description": lambda data: data['current_condition'][0]['weatherDesc'][0]['value'],
    "wind_speed": lambda data: f"{data['current_condition'][0]['windspeedKmph']} км/ч",
    "pressure": lambda data: f"{data['current_condition'][0]['pressure']} hPa",
}

def get_weather(city: str):
    url = f"https://wttr.in/{city}?format=j1"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Ошибка при получении данных:", e)
        sys.exit(1)

def show_options():
    print("Доступные поля:")
    for field in AVAILABLE_FIELDS:
        print(f" - {field}")
    sys.exit(0)

def main():

    args = parser.parse_args()

    if args.options:
        show_options()

    weather_data = get_weather(args.city)

    print(f"\nweather in : {args.city}")

    if args.field:
        field = args.field.lower()
        if field in AVAILABLE_FIELDS:
            result = AVAILABLE_FIELDS[field](weather_data)
            print(f"{field.capitalize()}: {result}")
        else:
            print(f"Unknown field: {field}")
            print("Use --options to see the list of available fields")
    else:
        for key, extractor in AVAILABLE_FIELDS.items():
            print(f"{key.capitalize()}: {extractor(weather_data)}")

if __name__ == "__main__":
    main()