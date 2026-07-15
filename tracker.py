def main():
    user_name = input("Enter Your Name: ").strip().title()
    bank_balance = int(input("Enter Your initial Bank Balance: "))
    print(f"Welcome {user_name}, your initial bank balance is: {bank_balance}")

    action = input("Do you want to deposit or withdraw? ").strip().upper()
    if action == "WITHDRAW":
        withdrawal = float(input("How much do you want to withdraw: "))

        #Overdraft protection
        if withdrawal > bank_balance:
            print("Insufficient funds.")
        else:
            bank_balance = withdraw(bank_balance, withdrawal)
            print("Withdraw Successful! your remaining balance is:", bank_balance)
    elif action == "DEPOSIT":
        deposit_amount = float(input("How much do you want to deposit: "))
        if deposit_amount > 0:
            bank_balance = deposit(bank_balance, deposit_amount)
            print("Deposit successful, your bank balance is:",bank_balance)
        else:
            print("Enter correct amount.")
    else:
        print("Invalid Action.")
    print(bank_balance)

def deposit(balance, amount):
    balance += amount
    return balance

def withdraw(balance, amount):
    balance -= amount
    return balance

def format_currency(amount):
    return f"${amount:,.2f}"    

main()