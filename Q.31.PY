### Q.31 Explain access specifiers in python.

# Access specifiers define how and where class variables and methods can be accessed.
# Python has three types of access specifiers:

### 1. Public Access Specifier

'''Accessible from anywhere (inside or outside the class).
By default, all variables and methods are public.

Example:'''

class Student:
    def __init__(self, name):
        self.name = name   # public variable

    def show(self):        # public method
        print(self.name)

s = Student("Shankar")
print(s.name)     # Accessible
s.show()          # Accessible

### 2. Protected Access Specifier

'''Defined using single underscore (_).
Accessible inside the class and its child class.
It is a convention, not strict protection.

Example:'''


class Student:
    def __init__(self, name):
        self._name = name   # protected variable

class Child(Student):
    def display(self):
        print(self._name)

c = Child("Shankar")
c.display()       # Allowed
print(c._name)    # Allowed but not recommended

### 3. Private Access Specifier

'''Defined using double underscore (__).
Accessible only inside the same class.
Python uses name mangling to protect it.

Example:'''

class Student:
    def __init__(self, name):
        self.__name = name   # private variable

    def show(self):
        print(self.__name)

s = Student("Shankar")
s.show()           # Allowed
# print(s.__name)  ❌ Error

print(s._Student__name)





