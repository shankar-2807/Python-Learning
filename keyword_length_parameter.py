#1.we can pass multiple attributes and values to the function
#2, use ** before variable name to store passed pairs(parameter)
#3. passed pair we will be stored as a dictionary formant
#4. use for loop to retrieve items from the dictionary
#5. use two(2) variables in for loop to fetch attributes & value seperately.

def emp(**data):
    for attr, val in data.item():
        print(f'{attr} : {val}')

emp(eid=101, ename='Akshay Kumar', sal= 45000, dept='Software Development')
print("####################################################")
emp(eid=102, ename='Allu Arjun', sal=15000, add='FC road,pune', email='ab@gmail.com')


