#### Simple example with self & method name 

class student:
    def set_details(self,name,branch):
        self.name = name
        self.branch = branch
        print(f'the student {self.name} is take admission {self.branch} course')


stud1 = student()
stud1.set_details('shankar','python')

stud2 = student()
stud2.set_details('pratik','java')


#### Simple example with __init__ method 

class student1:
    def __init__(self,name,branch):
        self.name = name
        self.branch = branch
        print(f'the student {self.name} is take admission {self.branch} course')

stud1 = student1('sagar','java')
stud2 = student1('ritesh','testing')



####  Encapsulation


class Bank:
    def __init__(self,name,balance):
        self.name = name
        self.__balance= balance

    def deposit(self,amount):
        self.__balance += amount
        print(f'deposit amount {amount} current balance is {self.__balance}')

    def showdetails(self):
        return self.__balance
        


balance = Bank('shankar',5000)
balance.deposit(2000)

balance.showdetails()


####  Abstraction  

from abc import ABC, abstractmethod

class Vehical(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehical):
    def start(self):
        print('Car Start with key...')

class Bike(Vehical):
    def start(self):
        print("Bike start with Button..")


car = Car()
bike = Bike()

car.start()
bike.start()


####  Polymorphism

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

a1 = Dog()
a2 = Cat()

a1.sound()
a2.sound()


####  inheritance

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

# Child class
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

# Creating objects
animal = Animal("Generic Animal")
dog = Dog("Buddy")

# Calling methods
animal.speak()  # Output: Generic Animal makes a sound
dog.speak()     # Output: Buddy says Woof!


