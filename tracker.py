def main():
    user_name = input("Enter Your Name: ").strip().title()
    bank_balance = int(input("Enter Your Bank Balance: "))
    print(f"Welcome {user_name}")

    action = input("Do you want to deposit or withdraw? ").strip().upper()
    if action == "WITHDRAW":
        withdrawal = float(input("How much do you want to withdraw: "))
        print("Withdraw successful your ramining balance is:", withdraw(bank_balance, withdrawal))
    elif action == "DEPOSIT":
        deposit_amount = float(input("How much do you want to deposit: "))
        print("Deposit successful, you are bank balance is:",deposit(bank_balance, deposit_amount))
    else:
        print("Invalid Action.")

def deposit(balance, amount):
    balance += amount
    return balance

def withdraw(balance, amount):
    balance -= amount
    return balance

def format_currency(amount):
    return f"${amount:,.2f}"    

main()