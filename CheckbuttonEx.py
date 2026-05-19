from tkinter import *
from tkinter import messagebox

def Submit():
    py_val = x.get()
    jv_val = y.get()
    test_val = z.get()

    course = ''

    if(py_val == 1):
        course += "Python\n"
    if(jv_val == 1):
        course += "Java\n"
    if(test_val == 1):
        course += "Testing"
    # print("Course:", course)
    messagebox.showinfo("Output", course)

if(__name__ == "__main__"):
    window = Tk()
    window.geometry("300x400")
    window.title("Checkbutton demo")

    x = IntVar()
    y = IntVar()
    z = IntVar()

    txt = Label(window, text="Please select course: ")
    py = Checkbutton(window, text="Pyrhon", variable=x)
    jv = Checkbutton(window, text="Java", variable=y)
    test = Checkbutton(window, text="Testing", variable=z)
    btn = Button(window, text="Submit", command = Submit)

    txt.grid(row=1, column=1)
    py.grid(row=2, column=1)
    jv.grid(row=2, column=2)
    test.grid(row=2, column=3)
    btn.grid(row=3, column=1, columnspan=3)

    window.mainloop()

