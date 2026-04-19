class BankAccount:
    def __init__(self, account_number, account_name, balance=0):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} to account {self.account_number}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.account_number}. New balance: {self.balance}")

    def get_balance(self):
        print(f"Account {self.account_number} balance: {self.balance}")

    def transfer(self, amount, recipient_account):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            recipient_account.balance += amount
            print(f"Transferred {amount} from account {self.account_number} to account {recipient_account.account_number}")

class Customer:
    def __init__(self, customer_id, customer_name):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.accounts = []

    def create_account(self, account_number, account_name, balance=0):
        new_account = BankAccount(account_number, account_name, balance)
        self.accounts.append(new_account)
        print(f"Account {account_number} created for customer {self.customer_name}")

    def get_accounts(self):
        for account in self.accounts:
            print(f"Account {account.account_number} - {account.account_name}")

class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.customers = []

    def create_customer(self, customer_id, customer_name):
        new_customer = Customer(customer_id, customer_name)
        self.customers.append(new_customer)
        print(f"Customer {customer_name} created")

    def get_customers(self):
        for customer in self.customers:
            print(f"Customer {customer.customer_id} - {customer.customer_name}")

bank = Bank("Example Bank")
bank.create_customer(1, "John Doe")
bank.create_customer(2, "Jane Doe")
customer1 = bank.customers[0]
customer2 = bank.customers[1]
customer1.create_account(12345, "John's account")
customer2.create_account(67890, "Jane's account")
customer1_accounts = customer1.accounts
customer2_accounts = customer2.accounts
customer1_accounts[0].deposit(1000)
customer2_accounts[0].deposit(500)
customer1_accounts[0].get_balance()
customer2_accounts[0].get_balance()
customer1_accounts[0].transfer(200, customer2_accounts[0])
customer1_accounts[0].get_balance()
customer2_accounts[0].get_balance()