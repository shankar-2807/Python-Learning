######Destructor:
#1. called when scope of object is done.
#2. Used to close database connections, network port. allocated resources.

class Student:
    def __init__(self, roll_no, name, percentage):
        self.roll_no = roll_no
        self.name = name
        self.perc = percentage

    def showData(self):
        return f'Roll No:{self.roll_no}\nName:{self.name}\nPercentage:{self.perc}'
    
    def __del__(self):
        print("Destructor Called.")

stud1 = Student(1, "Shankar", 98.00)
print(stud1.showData())

