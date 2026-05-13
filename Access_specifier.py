class Emp:
    def __init__(self, id, name, sal):
        self.eid = id       #public
        self._ename = name   #protected
        self.__sal = sal    #private

    def disply(self):
        print(self.__sal)

e1 = Emp(101, "Shankar", 98000)

print(e1.eid)
print(e1._ename)     #Not working in python.
#print(e1.__sal)    #Gives Error

e1.disply()