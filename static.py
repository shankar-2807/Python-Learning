class Employee:
    total_emp = 0

    def __init__(self, id, name, sal):
        Employee.total_emp = Employee.total_emp + 1
        self.eid = id
        self.ename = name
        self.sal = sal

    def Display(self):
        print("This is display method.")

e1 = Employee(101, "Rohit", 45000)

e2 = Employee(102, "Pratik", 50000)

print("Total employee: ", Employee.total_emp)

