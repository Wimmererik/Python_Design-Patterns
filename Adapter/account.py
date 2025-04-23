### Account class to store balances


class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        return True
    
    def __str__(self):
        return f"{self.name}: ${self.balance}"
