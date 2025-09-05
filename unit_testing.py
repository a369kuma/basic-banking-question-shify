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







# Unit Testing
import unittest

class TestAccount(unittest.TestCase):
    def setUp(self):
        # Create a new account instance before each test
        self.account = Account()

    def test_initial_balance(self):
        # Test that the initial balance is zero
        self.assertEqual(self.account.balance, 0.0)

    def test_deposit_positive_amount(self):
        # Test depositing a positive amount
        self.account.deposit(100.0)
        self.assertEqual(self.account.balance, 100.0)

    def test_deposit_negative_amount(self):
        # Test depositing a negative amount (should not change balance)
        self.account.deposit(-50.0)
        self.assertEqual(self.account.balance, 0.0)

    def test_withdraw_positive_amount(self):
        # Test withdrawing a valid amount
        self.account.deposit(100.0)
        self.account.withdraw(50.0)
        self.assertEqual(self.account.balance, 50.0)

    def test_withdraw_insufficient_balance(self):
        # Test withdrawing more than the available balance
        self.account.deposit(50.0)
        self.account.withdraw(100.0)
        self.assertEqual(self.account.balance, 50.0)

    def test_withdraw_negative_amount(self):
        # Test withdrawing a negative amount (should not change balance)
        self.account.withdraw(-30.0)
        self.assertEqual(self.account.balance, 0.0)

    def test_transaction_history(self):
        # Test that transaction history is recorded correctly
        self.account.deposit(100.0)
        self.account.withdraw(50.0)
        self.assertEqual(len(self.account.transaction_history), 2)
        self.assertEqual(self.account.transaction_history[0], {"type": "deposit", "amount": 100.0})
        self.assertEqual(self.account.transaction_history[1], {"type": "withdrawal", "amount": 50.0})

if __name__ == "__main__":
    unittest.main()

