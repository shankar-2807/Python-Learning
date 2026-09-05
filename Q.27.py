## Q.27  What is static variable and method & how to implement it. 

'''
Static Variable and Static Method in Python (with implementation)
🔹 Static Variable (Class Variable)

It is shared by all objects of the class.
Declared inside the class but outside methods.

🔹 Static Method

A static method is a method that does not use self .
Defined using the decorator @staticmethod.
Can be called using class name or object name.
'''
class Student:
    college = "ABC Institute"   # static variable

    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name, Student.college)

    @staticmethod
    def info():
        print("This is Student class")


s1 = Student("Shankar")
s2 = Student("Pragati")

s1.show()
s2.show()

Student.info()



