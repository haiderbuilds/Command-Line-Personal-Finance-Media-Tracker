import sys

def deposit(balance, amount):
    balance += amount
    return balance

def withdraw(balance, amount):
    balance -= amount
    return balance

def format_currency(amount):
    return f"${amount:,.2f}"

def get_float(prompt):
        try:
            while True:
                amount = float(input(prompt))
                return amount
        except ValueError:
            print("Invalid input. Please enter a number.")
        except EOFError, KeyboardInterrupt:
            pass

def main():
    transactions = []
    username = sys.argv[1].strip().title()
    bank_balance = float(sys.argv[2])
    print(f"Welcome {username}, Your initial bank balance is: {format_currency(bank_balance)}")
    while True:
        action = input("Do you want to deposit or withdraw? ").strip().lower()
        if action == "withdraw":
            withdrawal = get_float("How much do you want to withdraw? ")
            category = input("What is the purpose of this transaction? ").strip().lower()

            if withdrawal > bank_balance:
                print("Insufficient funds.")
            else:
                match category:
                    case "rent":
                        necessity_level = "High"
                    case "food":
                        necessity_level = "High"
                    case "entertainment":
                        necessity_level = "Low"
                    case "clothes":
                        necessity_level = "Medium"
                    case _:
                        necessity_level = "Unknown"
                print("Necessity level:", necessity_level)

                bank_balance = withdraw(bank_balance, withdrawal)
                print("Transaction Successful! Your remaining bank balance is:", format_currency(bank_balance))
                transactions.append({"type": "withdraw", "category": category, "amount": withdrawal})
        elif action == "deposit":
            deposit_amount = get_float("How much do you want to deposit? ")
            if deposit_amount > 0:
                bank_balance = deposit(bank_balance, deposit_amount)
                print("Transaction Successful! Your bank balance is:",format_currency(bank_balance))
                transactions.append({"type": "deposit", "amount": deposit_amount})
            else:
                print("Enter a correct amount.")
        elif action == "report":
            total_amount = 0
            print("\n--- Transaction Report ---")

            for transaction in transactions:
                print(f"type: {transaction["type"]}, amount: {format_currency(transaction["amount"])}")
                total_amount += transaction["amount"]
            print("\n Toatl transactions =", len(transactions))
            print("Total amount spent =", format_currency(total_amount))

        elif action == "quit":
            break
        else:
            print("Invalid Action, Try Again.")
        print("Closing balance", format_currency(bank_balance))

main()