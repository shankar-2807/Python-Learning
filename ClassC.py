from ClassA import A
from ClassB import B

class C(A, B):
    def __init__(self):
        print("This is Constructor of C.")

    def method(self):
        print("This is method of C.")

c1 = C
c1.get()
c1.showData()
c1.disply()





