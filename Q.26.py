## Q.26 Explain abstract class & method.

'''
Abstract Class & Abstract Method (Python)
1️⃣ Abstract Class


It is used as a blueprint for other classes.
In Python, abstract classes are created using the abc module.

2️⃣ Abstract Method

An abstract method is a method that is declared but not defined in the abstract class.
It only has a method name, no body (logic).
Abstract methods are created using the @abstractmethod decorator.
'''

from abc import ABC, abstractmethod

# Abstract Class
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass




