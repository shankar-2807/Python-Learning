from tkinter import *

def add():
    n1 = int(num1.get())
    n2 = int(num2.get())
    sum = n1 + n2
    output.configure(text="Addition:"+str(sum))


if(__name__ == "__main__"):
    window = Tk()
    window.geometry("300x400")
    window.title("Addition")

    txt1 = Label(window, text="Enter number 1:")
    num1 = Entry(window)

    txt2 = Label(window, text="Enter number 2:")
    num2 = Entry(window)

    btn = Button(window, text="ADD", command=add)
    output = Label(window, text="")

    txt1.grid(row=1,column=1)
    num1.grid(row=1, column=2)
    txt2.grid(row=2,column=1)
    num1.grid(row=2, column=2)

    btn.grid(row=3, column=1, columnspan=2)
    output.grid(row=4, column=1, columnspan=2)
    
    window.mainloop()


