class Bill:
    def __init__(self, pen, notebook, book, campass, pad):
        self.p = pen
        self.n = notebook
        self.b = book
        self.c = campass
        self.p = pad

    def Total_bill(self):
        print("Total_Bill: ", self.p + self.n + self.b + self.c + self.p)

Discount_Bill = Bill() * 15 / 100
print(Discount_Bill)

