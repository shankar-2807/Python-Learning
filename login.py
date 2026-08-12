import getpass
from helpers import prompt_nonempty, find_by_key
from principal import principal_password, students
from menus import principal_menu, student_menu

def principal_login():
    pwd = getpass.getpass("Enter Principal Password: ")
    if pwd == principal_password:
        principal_menu()
    else:
        print("Incorrect password!")

def student_login():
    roll = prompt_nonempty("Enter Roll No: ")
    st = find_by_key(students, "roll", roll)
    if not st:
        print("Student not found! Ask Principal to add your account.")
        return
    pwd = getpass.getpass("Enter Password: ")
    if pwd != st.get("password"):
        print("Incorrect password!")
        return
    student_menu(st)

