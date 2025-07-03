import argparse
import requests
import time
import os


def parse_arguments():
    parser = argparse.ArgumentParser(description="Crypto Statistics CLI")
    parser.add_argument("-n", "--name", help="Filter by coin name")
    parser.add_argument("-p", "--price", type=float, help="Filter by min price (USD)")
    return parser.parse_args()


def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 15,
        "page": 1,
        "sparkline": "false"
    }
    response = requests.get(url, params=params)
    return response.json()


def filter_coins(coins, name_filter=None, price_filter=None):
    filtered = []

    for coin in coins:
        name_match = True
        price_match = True

        if name_filter:
            name_match = name_filter.lower() in coin["name"].lower()

        if price_filter is not None:
            price_match = coin["current_price"] > price_filter

        if name_match and price_match:
            filtered.append(coin)

    return filtered


def display_coins(coins):
    for coin in coins:
        print(f"Name: {coin['name']}")
        print(f"Symbol: {coin['symbol']}")
        print(f"Current Price: ${coin['current_price']}")
        print(f"Market Cap: ${coin['market_cap']}")
        print(f"Total Volume: ${coin['total_volume']}")
        print(f"Price Change (24h): {coin['price_change_percentage_24h']}%")
        print('-' * 40)


def main():
    args = parse_arguments()

    while True:
        os.system('cls')

        try:
            data = fetch_crypto_data()

            if not isinstance(data, list):
                print("Error: API returned unexpected format.")
                print(data)
                break

            filtered = filter_coins(data, args.name, args.price)

            if filtered:
                display_coins(filtered)
            else:
                print("There are no coins that match the filters.")
                break
        except Exception as e:
            print("Error while receiving data:", e)
            break
        time.sleep(5)

if __name__ == "__main__":
    main()
