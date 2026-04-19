class BankAccount:
    def __init__(self, account_number, account_name, balance=0):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Current balance is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. Current balance is {self.balance}")

    def check_balance(self):
        print(f"Current balance is {self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_name, balance=0, interest_rate=0.05):
        super().__init__(account_number, account_name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount
        print(f"Added interest of {interest_amount}. Current balance is {self.balance}")

class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_name, balance=0, overdraft_limit=1000):
        super().__init__(account_number, account_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print("Transaction exceeded overdraft limit")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. Current balance is {self.balance}")

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_name, account_type, balance=0):
        if account_type == "Savings":
            self.accounts[account_number] = SavingsAccount(account_number, account_name, balance)
        elif account_type == "Current":
            self.accounts[account_number] = CurrentAccount(account_number, account_name, balance)
        else:
            print("Invalid account type")

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def list_accounts(self):
        for account in self.accounts.values():
            print(f"Account Number: {account.account_number}, Account Name: {account.account_name}, Balance: {account.balance}")

bank = Bank()
bank.create_account("12345", "John Doe", "Savings", 1000)
bank.create_account("67890", "Jane Doe", "Current", 500)
account1 = bank.get_account("12345")
account1.deposit(500)
account1.check_balance()
account2 = bank.get_account("67890")
account2.withdraw(200)
account2.check_balance()
bank.list_accounts()