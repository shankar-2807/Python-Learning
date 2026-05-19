from Account import Account
class CurrentAccount(Account):
    def __init__(self, ac_no, name, balance):
        super().__init__(ac_no, name)
        self.ac_type = "Current"
        self.balance = balance
    
    def __str__(self):
        data = super().__str__()
        return f'{data}, {self.ac_type}, {self.balance}'

# s1 = SavingAccount(75001, "Ranjeet Kamble", 30000)
# print(s1)

