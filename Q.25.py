### Q.25  What is method overloading / overriding.

#Method Overloading

'''Definition:
Method Overloading means same method name but different parameters (number or type).
In Python, method overloading is not directly supported, but we achieve it using default arguments .

Example (Overloading style in Python)'''
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(5))        # 5
print(calc.add(5, 10))    # 15
print(calc.add(5, 10, 2)) # 17



#Method Overriding

'''Definition:
Method Overriding means child class provides its own implementation of a method that already exists in the parent class.
Example (Overriding)'''

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

a = Animal()
d = Dog()
c = Cat()

a.sound()
d.sound()
c.sound()




