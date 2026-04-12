def addStudent(stud):
    roll_no = int(input("Enter roll no: "))
    name = input("Enter a name:")
    perc = float(input("Enter Percentage: "))
    add = input("Enter city: ")
    mob = int(input("Enter mob no: "))
    st = f'{roll_no}, {name}, {perc}, {add}, {mob}'
    stud[roll_no] = st

    print("Student added Successfully. ")
    return stud


def updateStudent(stud):
    roll_no = int(input("Enter roll no: "))
    studData = stud[roll_no]
    studList = studData.split(', ')

    checkNM = input("Do you want to change name(y/n):")
    if(checkNM.lower() in ['y', 'yes']):
        name = input(input("Enter name:"))
    else:
        name = studList[1]

    checkPerc = input("Do you want to change percentage(y/n):")
    if(checkPerc.lower() in ['y', 'yes']):
        perc = input(input("Enter name:"))
    else:
        perc = studList[2]

    checkAdd = input("Do you want to change address(y/n):")
    if(checkAdd.lower() in ['y', 'yes']):
        Address = input(input("Enter name:"))
    else:
        Address = studList[3]

    checkMn = input("Do you want to change mo.no.(y/n):")
    if(checkNM.lower() in ['y', 'yes']):
        Mn = input(input("Enter name:"))
    else:
        Mn = studList[4]

    st = f'{studList[0]}, {name}, {perc}, {Address} {Mn}'
    stud[roll_no] = st
    print("Data Updated Successfully.")
    return stud


stud = {}
ch = 0

while (ch != '6'):
    print('''Please choose option from below:
     1. Add student
     2. Update student
     3. Search student
     4. Show all student
     5. Delete student
     6. Exit''')
    ch = input("Enter choice:")
    if (ch == '1'):
        stud = addStudent(stud)
    elif(ch == '4'):
        print(stud)


  