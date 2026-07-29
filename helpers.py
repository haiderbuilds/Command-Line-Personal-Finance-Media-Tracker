import sys
import requests

def format_currency(amount):
    return f"${amount:,.2f}"

def get_float(prompt):
    while True:
        try:
            amount = float(input(prompt))
            return amount
        except ValueError:
            print("Invalid input. Please enter a number.")
        except (EOFError, KeyboardInterrupt):
            print("\nExiting program gracefully...")
            sys.exit()

def buy_song(artist_name, bank_balance):
    try:
        response = requests.get(
            "https://itunes.apple.com/search",
            params={
                "entity": "song",
                "limit": 1,
                "term": artist_name
            }
        )
        response.raise_for_status()
        data = response.json()

        if data["results"]:
            result = data["results"][0]
            track_price = float(result.get("trackPrice", 0))

            if bank_balance >= track_price:
                bank_balance -= track_price
                print(f"Purchased: {result['trackName']}")
            else:
                print("Insufficient balance")
        else:
            print("No songs found")
            
    except requests.RequestException:
        print("Error connecting to iTunes. Please check your internet connection.")

    return bank_balance