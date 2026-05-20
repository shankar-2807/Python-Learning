from tkinter import *
def addEmp():
    id = idTxt.get()
    name = nmTxt.get()
    sal = salTxt.get()
    dept = deptTxt.get()

    eData = f'{id}, {name}, {sal}, {dept}'
    with open("PYTHON/Tinker/empDetail.txt", "a") as fp:
        fp.write(eData+"\n")
    
    myList.insert(END, eData)

    clearData()

def clearData():
    idTxt.delete(0, END)
    nmTxt.delete(0, END)
    salTxt.delete(0, END)
    deptTxt.delete(0, END)
    idTxt.focus()
    
def selEmp():
    data = myList.get(ACTIVE)
    eList = data.split(", ")
    idTxt.insert(0, eList[0])
    nmTxt.insert(0, eList[1])
    salTxt.insert(0, eList[2])
    deptTxt.insert(0, eList[3])

def updEmp():
    id = idTxt.get()
    name = nmTxt.get()
    sal = salTxt.get()
    dept = deptTxt.get()
    allEmp = []
    
    with open("Course/March_April/TkinterDemo/empdetails.txt", "a") as fp:
        for line in fp:
            eList = line.split(", ")
            if(id == eList[0]):
                eStr = f'{id}, {name}, {sal}, {dept}'
            else:
                allEmp.append(line)


def delEmp():
    pass

if(__name__ == "__main__"):
    window = Tk()
    window.title("Employee details")
    window.geometry("300x400")

    frame1 = Frame(window)
    frame2 = Frame(window)
    frame3 = Frame(window)

    idLabel = Label(frame1, text="ID:")
    idTxt = Entry(frame1)
    nmLabel = Label(frame1, text="NAME:")
    nmTxt = Entry(frame1)
    salLabel = Label(frame1, text="SALARY:")
    salTxt = Entry(frame1)
    deptLabel = Label(frame1, text="DEPT:")
    deptTxt = Entry(frame1)

    idLabel.grid(row=1, column=1)
    idTxt.grid(row=1, column=2)
    nmLabel.grid(row=2, column=1)
    nmTxt.grid(row=2, column=2)
    salLabel.grid(row=3, column=1)
    salTxt.grid(row=3, column=2)
    deptLabel.grid(row=4, column=1)
    deptTxt.grid(row=4, column=2)
    frame1.pack()

    addBtn = Button(frame2, text="ADD", command=addEmp)
    selectBtn = Button(frame2, text="SELECT", command=selEmp)
    updBtn = Button(frame2, text="UPDATE", command=updEmp)
    delBtn = Button(frame2, text="DELETE", command=delEmp)

    addBtn.pack(side=LEFT)
    selectBtn.pack(side=LEFT)
    updBtn.pack(side=LEFT)
    delBtn.pack(side=LEFT)
    frame2.pack()

    scrollbar = Scrollbar(frame3)
    scrollbar.pack(side=RIGHT, fill=Y)
    myList = Listbox(frame3, yscrollcommand=scrollbar.set, height=15, width=40)
    myList.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command=myList.yview)
    frame3.pack()

    window.mainloop()

