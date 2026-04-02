class Vehical:
    def setData(self, brand, model, color, price):
        self.b = brand
        self.m = model
        self.c = color
        self.p = price

    def display(self):
        print("Brand:", self.b)
        print("Model:", self.m)
        print("Color:",self.c)
        print("Price:", self.p)

v1 = Vehical ()
v1.setData("Mercedes", "C200", "Black", 6500000)
v1.display()

print("####################################")

v2 = Vehical()
v2.setData("kia", "celtox", "white", 2500000)
v2.display()

print("####################################")
v3 = Vehical()
v3.setData("Innova", "IN2", "white", 3200000)
v3.display()


