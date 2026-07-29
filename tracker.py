import sys
import random
import helpers

def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    return balance - amount

def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py <username> <initial_balance>")
        sys.exit(1)

    username = sys.argv[1].strip().title()
    
    try:
        bank_balance = float(sys.argv[2])
    except ValueError:
        print("Error: Your initial balance must be a valid number.")
        sys.exit(1)

    transactions = []
    print(f"Welcome {username}, Your initial bank balance is: {helpers.format_currency(bank_balance)}")
    
    while True:
        try:
            action = input("\nDo you want to deposit, withdraw, report, gamble, buy song, or quit? ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting program gracefully...")
            break

        if action == "withdraw":
            withdrawal = helpers.get_float("How much do you want to withdraw? ")
            category = input("What is the purpose of this transaction? (rent, food, entertainment, clothes) ").strip().lower()

            if withdrawal > bank_balance:
                print("Insufficient funds.")
            else:
                match category:
                    case "rent" | "food":
                        necessity_level = "High"
                    case "clothes":
                        necessity_level = "Medium"
                    case "entertainment":
                        necessity_level = "Low"
                    case _:
                        necessity_level = "Unknown"
                print("Necessity level:", necessity_level)

                bank_balance = withdraw(bank_balance, withdrawal)
                print("Transaction Successful! Your remaining bank balance is:", helpers.format_currency(bank_balance))
                transactions.append({"type": "withdraw", "category": category, "amount": withdrawal})
        
        elif action == "deposit":
            deposit_amount = helpers.get_float("How much do you want to deposit? ")
            if deposit_amount > 0:
                bank_balance = deposit(bank_balance, deposit_amount)
                print("Transaction Successful! Your bank balance is:", helpers.format_currency(bank_balance))
                transactions.append({"type": "deposit", "amount": deposit_amount})
            else:
                print("Enter a positive amount.")
        
        elif action == "report":
            total_spent = 0
            print("\n--- Transaction Report ---")
            
            for transaction in transactions:
                print(f"Type: {transaction['type'].title()}, Amount: {helpers.format_currency(transaction['amount'])}")
                if transaction["type"] == "withdraw":
                    total_spent += transaction["amount"]
            
            print(f"Total transactions = {len(transactions)}")
            print(f"Total amount spent = {helpers.format_currency(total_spent)}")

        elif action == "gamble":
            if bank_balance < 10:
                print("You need at least $10 to gamble!")
            else:
                bank_balance -= 10
                chance = random.randint(1, 5)
                if chance == 4:
                    print("Congrats!!! You won $100.")
                    bank_balance += 100
                else:
                    print("Sorry! You did not win.")
        
        elif action == "buy song":
            artist_name = input("Enter artist's name: ")
            bank_balance = helpers.buy_song(artist_name, bank_balance)
            
        elif action == "quit":
            print("Exiting program gracefully...")
            break
            
        else:
            print("Invalid Action, Try Again.")
            
        print("Closing balance:", helpers.format_currency(bank_balance))

if __name__ == "__main__":
    main()