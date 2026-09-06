## Q. 23. Explain steps of OOP concept.


### Encapsulation
class Bank:
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance

    def deposit(self,amount):
        self.amount = amount 
        self.__balance += amount

    def get_balance(self):
        return (f'the deposit amount is {self.amount} current balance is {self.__balance}')    

name1 = Bank('shankar',5000)
name1.deposit(3000)

print(name1.get_balance())


