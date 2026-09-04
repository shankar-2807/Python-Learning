### Q.29 Explain constructor & destructor

'''
1️⃣ Constructor (__init__)

A constructor is a special method that is automatically called when an object is created.
It is used to initialize (assign values to) object variables.
In Python, the constructor method name is __init__.

Example:'''

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # print(self.name,self.age)
        
s1 = Student("Shankar", 21)

'''
2️⃣ Destructor (__del__)

A destructor is a special method that is called when an object is destroyed.
It is mainly used to release resources like memory, files, or database connections.
In Python, the destructor method name is __del__.

Example: '''

class Student:
    def __init__(self):
        print("Object Created")

    def __del__(self):
        print("Object Destroyed")

s1 = Student()
del s1


