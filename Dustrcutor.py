#### Static variable
#1. Class level variable
#2. Only one copy created
#3. Can be accessed using classs

class Circle:
    pi = 3.14

    def __init__(self, r):
        self.r = r

    def area(self):
        return f'Area of circle is {Circle.pi * (self.r ** 2)}'
        
c1 = Circle(4)
print(c1.area())



