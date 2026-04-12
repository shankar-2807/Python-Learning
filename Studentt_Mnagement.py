def addStudent(stud):
    roll_no = int(input("Enter roll no:"))
    name = input("Enter name:")
    perc = float(input("Enter percentage:"))
    add = input("Enter city:")
    mob = int(input("Enter mob no:"))
    st = f'{roll_no}, {name}, {perc}, {add}, {mob}'
    stud[roll_no] = st
    print("Student added successfully.")
    return stud

def updateStudent(stud):
    roll_no = int(input("Enter roll no:"))
    studData = stud[roll_no]
    studList = studData.split(', ')

    checkNM = input("Do you want to change name(y/n):")
    if(checkNM.lower() in ['y', 'yes']):
        name = input("Enter name:")
    else:
        name = studList[1]

    checkPerc = input("Do you want to change percentage(y/n):")
    if(checkPerc.lower() in ['y', 'yes']):
        perc = float(input("Enter percentage:"))
    else:
        perc = studList[2]
    
    checkAdd = input("Do you want to change address(y/n):")
    if(checkAdd.lower() in ['y', 'yes']):
        add = float(input("Enter address:"))
    else:
        add = studList[3]

    checkMn = input("Do you want to change mobile no.(y/n):")
    if(checkMn.lower() in ['y', 'yes']):
        # mn = float(input("Enter mobile no.:"))
        studList[4] = float(input("Enter mobile no.:"))
    # else:
    #     mn = studList[4]

    st = f'{studList[0]}, {name}, {perc}, {add}, {studList[4]}'
    stud[roll_no] = st
    print("Data updated successfully.")
    return stud


def searchStudent(stud, roll_no):
    res = stud.get(roll_no, "Student not found.")
    if(res != "Student not found."):
        studList = res.split(", ")
        print("Roll no: ", studList[0])
        print("Nmae: ", studList[1])
        print("Percentage: ", studList[2])
        print("Address: ", studList[3])
        print("Mobile No: ", studList[4])
    else:
        print(res)

def deleteStudent(stud, roll_no):
    if(roll_no in stud.keys()):
        stud.pop(roll_no)
        print("Data deleted successfully.")
    else:
        print("Student not found.")
    return stud

def showAll(stud):
    print("Roll No | Name | Percentage | Address | Mobile No. ")
    for st in stud.values():
        studList = st.split(", ")
        print(f'{studList[0]}  |  {studList[1]}  | {studList[2]}  | {studList[3]} | {studList[4]}')


stud = {}
ch = 0
while(ch != '6'):
    print('''Please choose option from below:
    1. Add student
    2. Update student
    3. Search student
    4. Show all student
    5. Delete student
    6. Exit''')
    ch = input("Enter choice:")
    if(ch == '1'):
        stud = addStudent(stud)
    elif(ch == '2'):
        stud = updateStudent(stud)
    elif(ch == '3'):
        roll_no = int(input("Enter roll no:"))
        searchStudent(stud, roll_no)
    elif(ch == '4'):
        #print(stud)
        showAll(stud)
    elif(ch == '5'):
        roll_no = int(input("Enter roll no:"))
        stud = deleteStudent(stud, roll_no)


