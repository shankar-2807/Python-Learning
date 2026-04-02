class Rectangle:
    def __init__(self, length , width):
        self.l = length
        self.w = width

    def Area(self):
        print("Area:", self.l*self.w)

r1 = Rectangle(5, 7)
r1.Area()



