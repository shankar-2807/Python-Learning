## Function / method overriding ( runtime polymorphism):
#Super class & Sub class having same name of method
#####

class Bank:
    def __init__(self, name, branch, ifsc_code):
        self.n = name
        self.b = branch
        self.i = ifsc_code

    def disply(self):
        print("....Method of Bank class....")
        print("Name:", self.n)
        print("Branch:", self.b)
        print("Ifsc_code:", self.i)

class GovernBank(Bank):
    def __init__(self, name, branch, ifsc_code, scheme):
        super().__init__(name, branch, ifsc_code)
        self.s = scheme

    def disply(self):
        print("....Method of GovernBank....")
        super().disply()
        print("Scheme:", self.s)

gov1 = GovernBank("SBI", "SHIVAJI NAGAR", "SBIN000123", "Mudra Yojna")
gov1.disply()




# HOME WORK
#Animal super class
#bog , cat , horse sub class




