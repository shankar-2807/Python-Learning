import getpass
from helpers import prompt_nonempty, find_by_key
from principal import principal_password, students
from menus import principal_menu, student_menu
from principal import principal_login, student_login  

def main():
    while True:
        print("""\nWelcome to College Management System
                1. Principal Login
                2. Student Login
                3. Exit """)
        choice = input("Enter choice: ").strip()
        if choice == "1":
            if principal_login():
                principal_menu()
        elif choice == "2":
            student = student_login()
            if student:
                student_menu(student)  
        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()

