from principal import SchoolSystem
from menus import Menus

def main():
    school = SchoolSystem()
    menus = Menus(school)

    while True:
        print("""\nWelcome to College Management System
                1. Principal Login
                2. Student Login
                3. Exit """)
        choice = input("Enter choice: ").strip()
        if choice == "1":
            if school.principal_login():
                menus.principal_menu()
        elif choice == "2":
            student = school.student_login()
            if student:
                menus.student_menu(student)
        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()

    