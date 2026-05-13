### it is use the object state.
# if you get the all object obf attribute.
class Emp:
    def __init__ (self, id, name, salary):
        self.eid = id
        self.ename = name
        self.sal = salary

e1 = Emp(101, "Shankar", 85000)
print(e1.__dict__)




