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



#Main Advancement
    def display_transaction_history(self):
        # Display the transaction history
        if not self.transaction_history:
            print("No transactions found.")
        else:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(f"- {transaction['type'].capitalize()}: ${round(transaction['amount'], 2)}")



#Filter Transaction History

    def filter_transaction_history(self, transaction_type: str = None):
        # Filter transaction history by type
        filtered_history = [
            transaction for transaction in self.transaction_history
            if transaction_type is None or transaction["type"] == transaction_type
        ]
        if not filtered_history:
            print("No transactions found for the specified filter.")
        else:
            print(f"Filtered Transaction History ({transaction_type if transaction_type else 'All'}):")
            for transaction in filtered_history:
                print(f"- {transaction['type'].capitalize()}: ${round(transaction['amount'], 2)}")

#Export Transaction History

    def export_transaction_history(self, file_format: str = "csv"):
        # Export transaction history to a file
        if not self.transaction_history:
            print("No transactions to export.")
            return
        if file_format == "csv":
            with open("transaction_history.csv", "w") as file:
                file.write("type,amount\n")
                for transaction in self.transaction_history:
                    file.write(f"{transaction['type']},{transaction['amount']}\n")
            print("Transaction history exported to transaction_history.csv")
        elif file_format == "json":
            import json
            with open("transaction_history.json", "w") as file:
                json.dump(self.transaction_history, file)
            print("Transaction history exported to transaction_history.json")
        else:
            print("Unsupported file format.")