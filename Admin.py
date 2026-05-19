from Saving import SavingAccount
from Current import CurrentAccount
global all_acc_data
all_acc_data = {}

class Admin:
    def __init__(self):
        ch = 0
        while(ch != '8'):
            print("#####Admin Login#####")
            print('''Please select option:
            1. New account
            2. Update account
            3. Withdraw
            4. Deposit
            5. Balance check
            6. Delete account
            7. Show all account
            8. Exit''')
            ch = input("Enter choice:")
            if(ch == '1'):
                ac_type = input("Enter account type(saving/current):")
                ac_no = int(input("Enter account no:"))
                name = input("Enter account holder name:")
                ac_bal = int(input("Enter account balance:"))
                if(ac_type.lower() == 'saving'): #saving, Saving, SAVING
                    s1 = SavingAccount(ac_no, name, ac_bal)
                    ac_data = str(s1)
                    all_acc_data[ac_no] = ac_data
                    print("Account successfully created...")
                else:
                    s1 = CurrentAccount(ac_no, name, ac_bal)
                    ac_data = str(s1)
                    all_acc_data[ac_no] = ac_data
                    print("Account successfully created...")
            elif(ch == '7'):
                print(all_acc_data)

a1 = Admin()

