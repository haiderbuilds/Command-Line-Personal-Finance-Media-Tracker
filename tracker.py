def main():
    user_name = input("Enter Your Name: ").strip().title()
    bank_balance = int(input("Enter Your Bank Balance: "))
    print(f"Welcome {user_name}, your bank balance is: {bank_balance}")

def deposit(balance, amount):
    balance += amount
    return balance



def withdraw(balance, amount):
    balance -= amount
    return balance

main()