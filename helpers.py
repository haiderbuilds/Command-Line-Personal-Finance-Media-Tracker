def format_currency(amount):
    return f"${amount:,.2f}"

def get_float(prompt):
        while True:
            try:
                amount = float(input(prompt))
                return amount
            except ValueError:
                print("Invalid input. Please enter a number.")
            except EOFError, KeyboardInterrupt:
                pass