def main():
    #user_name = input("Enter Your Name: ").strip().title()
   # bank_balance = int(input("Enter Your Bank Balance: "))
    #print(f"Welcome {user_name}, your bank balance is: {bank_balance}")
    print(format_currency(2000.6363))

def deposit(balance, amount):
    balance += amount
    return balance



def withdraw(balance, amount):
    balance -= amount
    return balance

def format_currency(amount):
    return f"${amount:,.2f}"
    







main()