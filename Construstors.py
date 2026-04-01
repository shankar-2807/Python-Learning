#Constructor
#1. Called automatically when object  of a class is created
# __init__

class Employee:
    def __init__(self, id, name, salary, dept):
        #print("Constructor called.")
        self.eid = id
        self.ename = name
        self.sal = salary
        self.dept = dept

    def display(self):
        print("Id:",self.eid)
        print("Name:",self.ename)
        print("Salary:",self.sal)
        print("Dept:", self.dept)

e1 = Employee("101", "Shankar", 50000, "Software")
e1.display()

print("################################")

e2 = Employee("102", "Pratik", 50000, "Web Developer")
e2.display()

