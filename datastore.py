from config import storage
import mysql.connector

class Datastore:
    def __init__(self):
        if(storage == 'Dictionary'):
            self.empdata = {}
        else:
            self.connectDB()
    
    def addData(self, emp):
        if(storage == 'Dictionary'):
            self.empdata[emp.id] = emp
        else:
            values = emp.toTuple()
            sql = 'insert into emp(id, name, sal, dept) values(%s, %s, %s, %s)'
            self.cursor.execute(sql, values)
            self.conn.commit()

        return 'Data added successfully.'
    
    def getData(self):
        if(storage == 'Dictionary'):
            return self.empdata.values()
        else:
            sql = 'select * from emp'
            self.cursor.execute(sql)
            self.empdata = self.cursor.fetchall()
            return self.empdata
    
    def searchData(self, id):
        if(storage == 'Dictionary'):
            if(id in self.empdata):
                data = self.empdata[id]
                return data.toTuple()
            else:
                return None
        else:
            sql = 'select * from emp where id = %s'
            self.cursor.execute(sql, (id,))
            self.empdata = self.cursor.fetchone()
            return self.empdata
    
    def updData(self, emp):
        if(storage == 'Dictionary'):
            self.empdata[emp.id] = emp
        else:
            sql = 'update emp SET name=%s, sal=%s, dept=%s where id=%s'
            self.cursor.execute(sql, (emp.name, emp.sal, emp.dept, emp.id))
            self.conn.commit()
        return 'Data updated successfully.'
    
    def delData(self, id):
        if(storage == 'Dictionary'):
            self.empdata.pop(id)
        else:
            sql = 'delete from emp where id=%s'
            self.cursor.execute(sql, (id,))
            self.conn.commit()
        return 'Data deleted successfully.'
    
    def connectDB(self):
        try:
            self.conn = mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                password = '1137',
                database = 'fbs'
            )
        except:
            # print('In except block')
            self.conn = mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                password = '1137'
            )
            sql = 'create database fbs'
            self.cursor = self.conn.cursor()
            self.cursor.execute(sql)
            self.cursor.close()
            self.conn.close()

            self.conn = mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                password = '1137',
                database = 'fbs'
            )

            sql = 'create table emp(id varchar(10), name varchar(50), sal int, dept varchar(50))'
            self.cursor = self.conn.cursor()
            self.cursor.execute(sql)

        else:
            # print('In else block')
            self.cursor = self.conn.cursor()   
        

if(__name__ == '__main__'):
    from employee import Employee
    ds = Datastore()

    eObj = Employee('101', 'Yash', 35000, 'Developer')
    ds.addData(eObj)
    # eObj = Employee('102', 'Aniket', 45000, 'Testing')
    # ds.addData(eObj)

    # print(ds.getData())

    eObj = Employee('101', 'Yashraj', 45000, 'Sw developer')
    print(ds.updData(eObj))
    # print(ds.getData())

    # ds.delData('101')
    # print(ds.getData())

    print(ds.searchData('101'))