import argparse
import requests
import sys


def arguments():
    parser = argparse.ArgumentParser(description="Weather forecast by city")
    parser.add_argument("city", help="City name (e.g. Yerevan)")
    parser.add_argument("-f", "--field", help="Show only a specific weather field")
    parser.add_argument("--options", action="store_true", help="Show available weather fields")
    return parser.parse_args()


def available_fields():
    return {
        "temperature": lambda data: f"{data['current_condition'][0]['temp_C']} °C",
        "feels_like": lambda data: f"{data['current_condition'][0]['FeelsLikeC']} °C",
        "humidity": lambda data: f"{data['current_condition'][0]['humidity']}%",
        "description": lambda data: data['current_condition'][0]['weatherDesc'][0]['value'],
        "wind_speed": lambda data: f"{data['current_condition'][0]['windspeedKmph']} км/ч",
        "pressure": lambda data: f"{data['current_condition'][0]['pressure']} hPa",
    }


def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error while receiving data:", e)
        sys.exit(1)


def show_options(fields):
    print("Available fields:")
    for field in fields:
        print(f" - {field}")
    sys.exit(0)


def show_weather(args, fields):
    if args.options:
        show_options(fields)

    weather_data = get_weather(args.city)

    print(f"\nweather in : {args.city}")

    if args.field:
        field = args.field.lower()
        if field in fields:
            result = fields[field](weather_data)
            print(f"{field.capitalize()}: {result}")
        else:
            print(f"Unknown field: {field}")
            print("Use --options to see the list of available fields")
    else:
        for key, extractor in fields.items():
            print(f"{key.capitalize()}: {extractor(weather_data)}")

def main():
    args = arguments()
    fields = available_fields()
    show_weather(args, fields)

if __name__ == "__main__":
    main()