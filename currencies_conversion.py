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

# import requests  # Import requests for API calls

class Account:
    def __init__(self):
        # Initialize the account with a balance of zero and an empty transaction history
        self.balance = 0.0
        self.transaction_history = []
    #     self.currencies = {"USD": 1.0}  # Default currency is USD with a 1:1 conversion rate
    #     self.currency_balances = {"USD": 0.0}  # Multi-currency balances

    # def add_currency(self, currency: str, rate: float):
    #     # Add a new currency with its conversion rate
    #     if currency not in self.currencies and rate > 0:
    #         self.currencies[currency] = rate
    #         self.currency_balances[currency] = 0.0
    #         print(f"Currency {currency} added with rate {rate}.")
    #     else:
    #         print("Invalid currency or rate.")

    # def deposit_in_currency(self, amount: float, currency: str):
    #     # Deposit money in a specific currency
    #     if currency in self.currencies and amount > 0:
    #         self.currency_balances[currency] += amount
    #         self.transaction_history.append({"type": "deposit", "amount": amount, "currency": currency})
    #         print(f"Deposited: {round(amount, 2)} {currency}")
    #     else:
    #         print("Invalid currency or amount.")

    # def withdraw_in_currency(self, amount: float, currency: str):
    #     # Withdraw money in a specific currency
    #     if currency in self.currency_balances and amount > 0:
    #         if self.currency_balances[currency] >= amount:
    #             self.currency_balances[currency] -= amount
    #             self.transaction_history.append({"type": "withdrawal", "amount": amount, "currency": currency})
    #             print(f"Withdrew: {round(amount, 2)} {currency}")
    #         else:
    #             print("Insufficient balance in the specified currency.")
    #     else:
    #         print("Invalid currency or amount.")

    # def convert_currency(self, amount: float, from_currency: str, to_currency: str):
    #     # Convert an amount from one currency to another
    #     if from_currency in self.currencies and to_currency in self.currencies and amount > 0:
    #         if self.currency_balances[from_currency] >= amount:
    #             conversion_rate = self.currencies[to_currency] / self.currencies[from_currency]
    #             converted_amount = amount * conversion_rate
    #             self.currency_balances[from_currency] -= amount
    #             self.currency_balances[to_currency] += converted_amount
    #             print(f"Converted {round(amount, 2)} {from_currency} to {round(converted_amount, 2)} {to_currency}.")
    #         else:
    #             print("Insufficient balance in the source currency.")
    #     else:
    #         print("Invalid currency or amount.")

    # def update_exchange_rates(self, api_url: str, api_key: str):
    #     # Fetch and update exchange rates from a live API
    #     try:
    #         response = requests.get(api_url, headers={"apikey": api_key})
    #         if response.status_code == 200:
    #             data = response.json()
    #             if "rates" in data:
    #                 for currency, rate in data["rates"].items():
    #                     if rate > 0:
    #                         self.currencies[currency] = rate
    #                 print("Exchange rates updated successfully.")
    #             else:
    #                 print("Invalid response format from the API.")
    #         else:
    #             print(f"Failed to fetch exchange rates. HTTP Status Code: {response.status_code}")
    #     except Exception as e:
    #         print(f"An error occurred while fetching exchange rates: {e}")

    # def check_all_balances(self):
    #     # Check balances in all currencies
    #     print("Balances:")
    #     for currency, balance in self.currency_balances.items():
    #         print(f"{currency}: {round(balance, 2)}")

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

