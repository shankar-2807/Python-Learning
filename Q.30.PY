#### Q.30 What is __str__ Method.

'''
What is __str__ method?

__str__ is a special (magic) method in Python.
It returns a human-readable string representation of an object.
It is automatically called when you use print(object).

'''
# Your code with __str__ method added

class student1:
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch

    def __str__(self):
        return f"The student {self.name} has taken admission in {self.branch} course"

stud2 = student1('sagar', 'java')
stud3 = student1('ritesh', 'testing')

print(stud2)
print(stud3)




