class Employee:
    def __init__(self, id, name, salary):
        self.eid = id
        self.ename = name
        self.sal = salary

    def __str__(self):
        return f'ID:{self.eid}\nName:{self.ename}\nSalary:{self.sal}'
    
e1 = Employee(101, "Shankar", 50000)
print(e1)

