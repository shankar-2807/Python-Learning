class Rectangle:
    def __init__(self, length , width):
        self.l = length
        self.w = width

    def Peri(self):
        print("Perimeter:", 2 * (self.l + self.w))

peri1 = Rectangle(5, 7)
peri1.Peri()


