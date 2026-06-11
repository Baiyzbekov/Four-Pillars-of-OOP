class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposite(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(100)
account.deposite(50)
print(account.get_balance())

# Encapsulation hides gata inside a class and provides controlled access through methods.
# The __balance attribute cannot be accessed directly from outside the class