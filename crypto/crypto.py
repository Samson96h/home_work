import argparse
import requests
import time
import os


parser = argparse.ArgumentParser(description="Crypto Statistics CLI")
parser.add_argument("-n", "--name", help="Filter by coin name")
parser.add_argument("-p", "--price", type=float, help="Filter by min price (USD)")
args = parser.parse_args()


def main():
    while True:
        os.system('cls')

        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": 15,
            "page": 1,
            "sparkline": "false"
        }

        try:
            response = requests.get(url, params=params)
            data = response.json()

            if not isinstance(data, list):
                print("Error: API returned not in list. Response:")
                print(data)
            else:
                flag = False

                for coin in data:
                    name_match = True
                    price_match = True

                    if args.name:
                        name_match = args.name.lower() in coin["name"].lower()

                    if args.price is not None:
                        price_match = coin["current_price"] > args.price

                    if name_match and price_match:
                        flag = True
                        print(f"Name: {coin['name']}")
                        print(f"Symbol: {coin['symbol']}")
                        print(f"Current Price: ${coin['current_price']}")
                        print(f"Market Cap: ${coin['market_cap']}")
                        print(f"Total Volume: ${coin['total_volume']}")
                        print(f"Price Change (24h): {coin['price_change_percentage_24h']}%")
                        print('-' * 40)

                if not flag:
                    print("There are no coins that match the filters.")
                    break

        except Exception as e:
            print("Error: while receiving data", e)

        time.sleep(5)

if __name__ == "__main__":
    main()