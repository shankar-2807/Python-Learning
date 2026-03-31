class Book:
    def __init__(self, id = "bk01", name = "Rich Dad Poor Dad", author = "Robin", pub_year = "2000"):
        self.bid = id
        self.bname = name
        self.bauthor = author
        self.pub_year = pub_year

    def DisplyBook(self):
        print("id:", self.bid)
        print("Name:", self.bname)
        print("Author:", self.bauthor)
        print("pub_year:", self.pub_year)
        print("###########################")

bk1 = Book()
bk1.DisplyBook()


bk2 = Book("bk02", 'Mritunjay', 'Shivaji Sawant', 1997)
bk2.DisplyBook()

bk3 = Book("bk03", 'Chhava', 'Shivaji ', 2014)
bk3.DisplyBook()

