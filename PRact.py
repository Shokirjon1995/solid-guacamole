class BankAccount:
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance

    def deposit(self, new_balance):
        self.balance += new_balance

    def cash(self,change_balance):
        self.balance -= change_balance

    def my_balance(self):
        return self.balance



user1 = BankAccount('Eshmat')
print(user1.name, user1.balance)
user1.deposit(200000)
print(user1.name, user1.balance)
user1.cash(50000)
print(user1.name,user1.my_balance())
