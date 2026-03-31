class Circle:
    def __init__(self, radius):
        self.r = radius
        
    def Area(self):
        print("Area of circle:", 3.14 * self.r)

r1 = Circle(5)
r1.Area()

