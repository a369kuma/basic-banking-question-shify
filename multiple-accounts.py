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


# 1. Multiple Accounts

# Expand the system to handle multiple accounts, each with a unique identifier.
# Implement a method to transfer funds between accounts.

# Further Expansions:
# 	•	Account Aggregation: Implement a method to get the total balance across
#      all accounts for a user, providing a summary of their financial status.
# 	•	Account Types: Introduce different types of accounts (e.g., checking, savings) 
#     with varied features such as interest rates and withdrawal limits.

class BankingSystem:
    def __init__(self):
        # Initialize a dictionary to store multiple accounts
        self.accounts = {}

    # 1. Multiple Accounts
    def create_account(self, account_id: str, account_type: str = "checking"):
        # Create a new account with a unique identifier and type
        if account_id in self.accounts:
            print("Account ID already exists.")
        else:
            self.accounts[account_id] = {"account": Account(), "type": account_type}
            print(f"Account '{account_id}' of type '{account_type}' created.")

    def transfer_funds(self, from_id: str, to_id: str, amount: float):
        # Transfer funds between two accounts
        if from_id not in self.accounts or to_id not in self.accounts:
            print("One or both account IDs do not exist.")
        elif amount <= 0:
            print("Transfer amount must be positive.")
        else:
            from_account = self.accounts[from_id]["account"]
            to_account = self.accounts[to_id]["account"]
            if from_account.balance >= amount:
                from_account.withdraw(amount)
                to_account.deposit(amount)
                print(f"Transferred ${round(amount, 2)} from '{from_id}' to '{to_id}'.")
            else:
                print("Insufficient balance in the source account.")

    # 2. Account Aggregation
    def get_total_balance(self):
        # Get the total balance across all accounts
        total_balance = sum(account["account"].balance for account in self.accounts.values())
        print(f"Total balance across all accounts: ${round(total_balance, 2)}")

    # 3. Account Types
    def get_account_type(self, account_id: str):
        # Get the type of a specific account
        if account_id in self.accounts:
            account_type = self.accounts[account_id]["type"]
            print(f"Account '{account_id}' is of type '{account_type}'.")
        else:
            print("Account ID does not exist.")

    system.get_account_type("acc2")





