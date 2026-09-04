### Q.28 


# class Bank():
#     def __init__(self,name,balance):
#         self.n = name
#         self.__balance = balance

#     def deposit(self,amount):
#         self.__balance += amount
#         print(f'deposit amount {amount} current balance is {self.__balance}')

#     def show_details(self):
#         return self.__balance
    

# balance = Bank('shankar',5000)
# balance.deposit(2000)

# balance.show_details


# class Bank():
#     def __init__(self,name,balance):
#         self.name = name
#         self.__balance = balance

#     def deposit(self,amount):
#         self.__balance += amount
#         print(f'deposit amount {amount} current balance is {self.__balance}')
        
#     def show_details(self):
#         return self.__balance


# e1 = Bank('shankar',5000)
# e1.deposit(2000)

# e1.show_details()


####  inheritance

# Parent class
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print(f"{self.name} makes a sound")

# # Child class
# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name} says Woof!")

# # Creating objects
# animal = Animal("Generic Animal")
# dog = Dog("Buddy")

# # Calling methods
# animal.speak()  # Output: Generic Animal makes a sound
# dog.speak()     # Output: Buddy says Woof!


class Animal():
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(f'{self.name} make a sound')


class Dog(Animal):
    def speak(self):
        print(f'{self.name} says woof!')


animal =Animal('generic animal')
dog = Dog('buddy')

animal.speak()
dog.speak()



def name ():
    print('My Name is Shankar')

name()


def age (a,b):
    c = a + b
    print(f'my age is {c}')

age(20,2)


def address(city='tuljapur',state='maharashtra'):
    print(f'i am leaving in {city}, {state}')

address()


def pin(x):
    return x

xx = pin(413601)
print(xx)





