from employee import Employee
from datastore import Datastore
from config import storage
class Admin:
    def __init__(self):
        self.ds = Datastore()
        ch = 0
        while(ch != '6'):
            print('''-----ADMIN-----
            1. Add employee
            2. Show all employee
            3. Search employee
            4. Update employee
            5. Delete employee
            6. Exit''')
            ch = input('Enter choice:')
            if(ch == '1'):
                self.addEmp()
            elif(ch == '2'):
                self.showAllEmp()
            elif(ch == '3'):
                self.searchEmp()
            elif(ch == '4'):
                self.updEmp()
            elif(ch == '5'):
                self.delEmp()
            elif(ch == '6'):
                print('Logged out...')
            else:
                print('Invalid choice...')
    
    def addEmp(self):
        id = input('Enter id:')
        name = input('Enter name:')
        sal = int(input('Enter salary:'))
        dept = input('Enter department:')
        eObj = Employee(id, name, sal, dept)
        res = self.ds.addData(eObj)
        print(res)

    def showAllEmp(self):
        res = self.ds.getData()
        for e in res:
            columns = ['id', 'name', 'sal', 'dept']
            if(storage == 'Dictionary'):
                for key, value in zip(columns, e.toTuple()):
                    print(key, ':', value)
            else:
                for key, value in zip(columns, e):
                    print(key, ':', value)
            print('######################')

    def searchEmp(self):
        id = input('Enter id:')
        res = self.ds.searchData(id)
        if(res):
            print(res)
        else:
            print('Employee not found.')

    def updEmp(self):
        id = input('Enter id:')
        res = self.ds.searchData(id)
        if(res):
            print('NOTE: Leave field empty if no need to change value.')
            eData = res
            name = input(f'Enter name({eData[1]}):') or eData[1]
            sal = input(f'Enter sal({eData[2]}):') or eData[2]
            dept = input(f'Enter dept({eData[3]}):') or eData[3]
            eObj = Employee(id, name, sal, dept)
            res = self.ds.updData(eObj)
            print(res)
        else:
            print('Employee not found.')

    def delEmp(self):
        id = input('Enter id:')
        res = self.ds.searchData(id)
        if(res):
            res = self.ds.delData(id)
            print(res)
        else:
            print('Employee not found.')

if(__name__ == '__main__'):
    aObj = Admin()