from tkinter import *
if (__name__ == "__main__"):
    window = Tk()

    window.geometry("300x400")
    window.title("First program")

    label = Label(window, text="Hello World!")
    label.grid(row=1,column=1)

    window.mainloop()

