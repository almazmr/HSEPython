class Account:
    def __init__(self, name, initial_balance):
        self.name = name
        self.balance = initial_balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited {amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew {amount}")
        else:
            print("Insufficient funds")

    def get_transaction_history(self):
        return self.transaction_history
    

account = Account("Almaz Kadikov", 1000)
account.deposit(900)
account.withdraw(400)
print(f"Balance '{account.name}' amounts to {account.balance}")  # Output: 1300
print(account.get_transaction_history())  # Output: ['Deposited 900', 'Withdrew 400']
