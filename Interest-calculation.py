# This script simulates a basic banking system with the following features:
# - Users can create an account with an initial balance of zero.
# - The account supports three main operations:
#   1. Checking the current balance.
#   2. Depositing money into the account.
#   3. Withdrawing money from the account.
# - Deposits and withdrawals are handled as floating-point numbers to ensure precision.
# - The system ensures that:
#   - Deposits must be positive amounts.
#   - Withdrawals cannot exceed the available balance.
#   - Withdrawals must also be positive amounts.
# - The application is interactive and allows users to perform these operations repeatedly.
# - The user can exit the application at any time.

class Account:
    def __init__(self):
        # Initialize the account with a balance of zero and an empty transaction history
        self.balance = 0.0
        self.transaction_history = []

    def deposit(self, amount: float):
        # Deposit money into the account
        if amount > 0:
            self.balance += amount
            self.transaction_history.append({"type": "deposit", "amount": amount})
            print(f"Deposited: ${round(amount, 2)}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount: float):
        # Withdraw money from the account
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount > 0:
            self.balance -= amount
            self.transaction_history.append({"type": "withdrawal", "amount": amount})
            print(f"Withdrew: ${round(amount, 2)}")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        # Check the current balance
        print(f"Current balance: ${round(self.balance, 2)}")

# Main Interest calc advancement

    def calculate_simple_interest(self, annual_rate: float, months: int):
        # Calculate and apply simple interest to the account balance
        if annual_rate < 0 or months <= 0:
            print("Invalid interest rate or duration.")
            return
        monthly_rate = annual_rate / 12 / 100
        interest = self.balance * monthly_rate * months
        self.balance += round(interest, 2)
        print(f"Applied simple interest: ${round(interest, 2)}")
        print(f"New balance: ${round(self.balance, 2)}")

#Compounding interest

    def calculate_compound_interest(self, annual_rate: float, months: int, compounding_frequency: int = 12):
        # Calculate and apply compound interest to the account balance
        if annual_rate < 0 or months <= 0 or compounding_frequency <= 0:
            print("Invalid interest rate, duration, or compounding frequency.")
            return
        monthly_rate = annual_rate / 12 / 100
        periods = months * (compounding_frequency / 12)
        compound_factor = (1 + monthly_rate / (compounding_frequency / 12)) ** periods
        interest = self.balance * (compound_factor - 1)
        self.balance += round(interest, 2)
        print(f"Applied compound interest: ${round(interest, 2)}")
        print(f"New balance: ${round(self.balance, 2)}")

#Interest rates based on tiers
    
    def calculate_tiered_interest(self, months: int):
        # Apply tiered interest rates based on the account balance
        if months <= 0:
            print("Invalid duration.")
            return
        if self.balance < 1000:
            annual_rate = 1.0  # 1% for balances below $1000
        elif self.balance < 5000:
            annual_rate = 2.0  # 2% for balances between $1000 and $5000
        else:
            annual_rate = 3.0  # 3% for balances above $5000
        self.calculate_simple_interest(annual_rate, months)


#Handling Floating Point Precision

    def handle_precision(self):
        # Ensure balance is rounded to two decimal places
        self.balance = round(self.balance, 2)
        print(f"Balance adjusted for precision: ${self.balance}")

