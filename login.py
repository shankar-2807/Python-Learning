import getpass
from helpers import Helper
from principal import principal_password, students
from menus import principal_menu, student_menu


class LoginSystem:
    def __init__(self):
        # imported values remain as references
        self.principal_password = principal_password
        self.students = students

    def principal_login(self):
        pwd = getpass.getpass("Enter Principal Password: ")
        if pwd == self.principal_password:
            principal_menu()
        else:
            print("Incorrect password!")

    def student_login(self):
        roll = Helper.prompt_nonempty("Enter Roll No: ")
        st = Helper.find_by_key(self.students, "roll", roll)
        if not st:
            print("Student not found! Ask Principal to add your account.")
            return
        pwd = getpass.getpass("Enter Password: ")
        if pwd != st.get("password"):
            print("Incorrect password!")
            return
        student_menu(st)

