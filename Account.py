class Account:
    def __init__(self, ac_no, name):
        self.ac_no = ac_no
        self.name = name
    
    def __str__(self):
        return f'{self.ac_no}, {self.name}'


ac1 = Account(75001, "Ranjeet Kamble")
print(ac1)

