class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, depos):
        self.balance += depos

    def withdraw(self, summ):
        if summ <= self.balance:
            self.balance -= summ
        else:
            print(f"{self.owner}, your balance is lower than you want to withdraw")

    def __str__(self):
        return f"{self.owner}'s balance is {self.balance}"


acc = Account('Boris', 1000)
print(acc)
acc.deposit(1000)
print(acc)
acc.deposit(200)
print(acc)
acc.withdraw(450)
print(acc)
acc.withdraw(10000)
