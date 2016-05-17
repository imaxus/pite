class BankAccount(object):
    def __init__(self, name="", initial_balance=0):
        self.balance = initial_balance
        self.name = name

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def overdrawn(self):
        return self.balance < 0

