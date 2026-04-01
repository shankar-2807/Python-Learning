class Employee:
    def __init__(self, id, name):
        self.eid = id
        self.ename = name

    def showData(self):
        print("Employee ID:", self.eid)
        print("Employee Name:", self.ename)

class Hr(Employee):
    def __init__(self, id, name, rec_target):
        super().__init__(id, name)
        self.rec_target = rec_target

    def showData(self):
        super().showData()
        print("Recruitment target:", self.rec_target)

h1 = Hr(101, "Shankar Mashalkar", 10)
h1.showData


