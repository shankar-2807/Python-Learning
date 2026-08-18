import os

class Student:
    def __init__(self, username, student_id):
        self.username = username
        self.student_id = student_id

    def menu(self):
        while True:
            print("\n--- Student Menu ---")
            print("1. Change password")
            print("2. Course: view/search/select")
            print("3. Notice: view/search")
            print("4. Staff: view/search")
            print("5. Logout")

            ch = input("Choose: ")
            if ch == '1':
                self.change_password()
            elif ch == '2':
                self.course_menu()
            elif ch == '3':
                self.notice_menu()
            elif ch == '4':
                self.staff_menu()
            elif ch == '5':
                print("Logging out...")
                break
            else:
                print("Invalid choice!")

    def course_menu(self):
        while True:
            print("\nCourse Actions: 1.viewall 2.search 3.select 4.back")
            ch = input("Choose: ")
            if ch == '1':
                self.view_all("courses.txt")
            elif ch == '2':
                self.search("courses.txt")
            elif ch == '3':
                cid = input("Enter Course ID to select: ")
                print(f"Course {cid} selected successfully!")
            elif ch == '4':
                break
            else:
                print("Invalid choice!")

    def staff_menu(self):
        while True:
            print("\nStaff Actions: 1.viewall 2.search 3.back")
            ch = input("Choose: ")
            if ch == '1':
                self.view_all("staff.txt")
            elif ch == '2':
                self.search("staff.txt")
            elif ch == '3':
                break
            else:
                print("Invalid choice!")

    def notice_menu(self):
        while True:
            print("\nNotice Actions: 1.viewall 2.search 3.back")
            ch = input("Choose: ")
            if ch == '1':
                self.view_all("notices.txt")
            elif ch == '2':
                self.search("notices.txt")
            elif ch == '3':
                break
            else:
                print("Invalid choice!")

    def change_password(self):
        new_pass = input("Enter new password: ")
        lines = open("credentials.txt").readlines()
        with open("credentials.txt", "w") as f:
            for line in lines:
                parts = line.strip().split("|")
                if parts[0] == self.username and parts[2] == "student":
                    parts[1] = new_pass
                    f.write("|".join(parts) + "\n")
                    print("Password changed successfully!")
                else:
                    f.write(line)

    def view_all(self, file):
        try:
            with open(file, "r") as f:
                data = f.readlines()
                if not data:
                    print("No records found.")
                for d in data:
                    print(d.strip())
        except FileNotFoundError:
            print("File not found!")

    def search(self, file):
        key = input("Enter keyword to search: ")
        try:
            with open(file, "r") as f:
                found = False
                for line in f:
                    if key.lower() in line.lower():
                        print(line.strip())
                        found = True
                if not found:
                    print("No matching record found.")
        except FileNotFoundError:
            print("File not found!")





