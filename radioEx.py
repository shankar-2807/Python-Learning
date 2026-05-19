from tkinter import *

def changeBg():
    rdoVal = x.get()
    if(rdoVal == 1):
        window.configure(bg="orange")
        info.destroy()
    elif(rdoVal == 2):
        window.configure(bg="blue")
        info.destroy()
    elif(rdoVal == 3):
        window.configure(bg="gray")
        info.destroy()
    else:
        info.configure(text="Please select color...")

if(__name__ == "__main__"):
    window = Tk()
    window.title("Radio Demo")
    window.geometry("300x400")

    x = IntVar()

    label1 = Label(window, text="Select color:")

    rdo1 = Radiobutton(window, text="Orange", variable=x, value=1)
    rdo2 = Radiobutton(window, text="Blue", variable=x, value=2)
    rdo3 = Radiobutton(window, text="Gray", variable=x, value=3)

    btn = Button(window, text="Submit", command=changeBg)

    info = Label(window, text="")

    label1.grid(row=1, column=1)
    rdo1.grid(row=2, column=1)
    rdo2.grid(row=2, column=2)
    rdo3.grid(row=2, column=3)
    btn.grid(row=3, column=1, columnspan=3)
    info.grid(row=4, column=1, columnspan=3)
    window.mainloop()

