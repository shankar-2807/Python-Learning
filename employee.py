class Employee:
    def __init__(self, id, name, sal, dept):
        self.id = id
        self.name = name
        self.sal = sal
        self.dept = dept
    
    def toTuple(self):
        return (self.id, self.name, self.sal, self.dept)

if(__name__ == '__main__'):
    e = Employee('101', 'Akash', 50000, 'Software developer')
    print(e.toTuple())