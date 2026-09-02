
class student ():
    def set_details(self,name,branch):
        self.name = name
        self.branch = branch
        print(f'the student {self.name} is take a admission on {self.branch} branch')


s1 = student()
s1.set_details('shankar','python')


class student():
    def __init__ (self,name,branch):
        self.name = name
        self.branch = branch
        print(f'the student {self.name} is take a admission on {self.branch} branch')


s1 = student('shankar','python')




class bank():
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance

    def deposit(self,amount):
        self.__balance += amount

        print (f'the deposit {amount} is current balance is {self.__balance}')

    def show_balance(self):
        return self.__balance
    

e1 = bank('shankar',5000)
e1.deposit(2000)
e1.show_balance()





class Animal():
    def __init__(self,name):
        self.name = name
        

    def speak(self):
        print(f'{self.name} make a sound')


class Dog(Animal):
    def speak(self):
        print(f'{self.name} says Woof!')


animal = Animal('generic animal')
dog = Dog('buddy')

animal.speak()
dog.speak()



