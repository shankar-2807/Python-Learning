class Account:
    total_amt = 0
    def __init__(self, acc_no, holdername, balance):
        self.acNo = acc_no
        self.hName = holdername
        self.bal = balance

        Account.total_amt += balance

    def showData(self):
        print("Account:", self.acNo)
        print("Holder Name:", self.hName)
        print("Balance:", self.bal)

    @staticmethod
    def ShowAllbal():
        print("Account N0:",Account.total_amt)

acc1 = Account(101, "Pratik", 50000)
acc1.showData()

print("#####################")

acc2 = Account(102, "Shankar", 100000)
acc2.showData()

print("#####################")
