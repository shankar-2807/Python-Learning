from principal import SchoolSystem
from student import StudentActions

class Menus:
    def __init__(self, school_system: SchoolSystem):
        self.school_system = school_system

    def principal_menu(self):
        while True:
            print("""
            Principal Menu:
            1. Change Password
            2. Course Management
            3. Staff Management
            4. Student Management
            5. Notice Management
            6. Logout
            """)
            ch = input("Enter choice: ").strip()
            if ch == "1":
                self.school_system.principal_change_password()
            elif ch == "2":
                self.course_menu()
            elif ch == "3":
                self.staff_menu()
            elif ch == "4":
                self.student_admin_menu()
            elif ch == "5":
                self.notice_menu()
            elif ch == "6":
                break
            else:
                print("Invalid choice!")

    def course_menu(self):
        while True:
            print("""
            Course Menu:
            1. Add Course
            2. Update Course
            3. Delete Course
            4. Show All Courses
            5. Search Course
            6. Back
            """)
            c = input("Enter choice: ").strip()
            if c == "1": self.school_system.add_course()
            elif c == "2": self.school_system.update_course()
            elif c == "3": self.school_system.delete_course()
            elif c == "4": self.school_system.search_course()
            elif c == "5": self.school_system.search_course()
            elif c == "6": break
            else: print("Invalid choice!")

    def staff_menu(self):
        while True:
            print("""
            Staff Menu:
            1. Add Staff
            2. Update Staff
            3. Delete Staff
            4. Show All Staff
            5. Search Staff
            6. Back
            """)
            c = input("Enter choice: ").strip()
            if c == "1": self.school_system.add_staff()
            elif c == "2": self.school_system.update_staff()
            elif c == "3": self.school_system.delete_staff()
            elif c == "4": self.school_system.search_staff()
            elif c == "5": self.school_system.search_staff()
            elif c == "6": break
            else: print("Invalid choice!")

    def student_admin_menu(self):
        while True:
            print("""
            Student (Admin) Menu:
            1. Add Student
            2. Update Student
            3. Delete Student
            4. Show All Students
            5. Search Student
            6. Back
            """)
            c = input("Enter choice: ").strip()
            if c == "1": self.school_system.add_student()
            elif c == "2": self.school_system.update_student()
            elif c == "3": self.school_system.delete_student()
            elif c == "4": self.school_system.search_student()
            elif c == "5": self.school_system.search_student()
            elif c == "6": break
            else: print("Invalid choice!")

    def notice_menu(self):
        while True:
            print("""
            Notice Menu:
            1. Add Notice
            2. Update Notice
            3. Delete Notice
            4. Show All Notices
            5. Search Notice
            6. Back
            """)
            c = input("Enter choice: ").strip()
            if c == "1": self.school_system.add_notice()
            elif c == "2": self.school_system.update_notice()
            elif c == "3": self.school_system.delete_notice()
            elif c == "4": self.school_system.search_notice()
            elif c == "5": self.school_system.search_notice()
            elif c == "6": break
            else: print("Invalid choice!")

    def student_menu(self, student):
        while True:
            print(f"Welcome {student['name']} ({student['roll']})")
            print("""
            Student Menu:
            1. Change Password
            2. Course: View All
            3. Course: Search
            4. Notice: View All
            5. Notice: Search
            6. Staff: View All
            7. Staff: Search
            8. Logout
            """)
            c = input("Enter choice: ").strip()
            if c == "1": StudentActions.change_password(student)
            elif c == "2": StudentActions.view_all_courses(self.school_system.courses)
            elif c == "3": StudentActions.search_course(self.school_system.courses)
            elif c == "4": StudentActions.view_all_notices(self.school_system.notices)
            elif c == "5": StudentActions.search_notice(self.school_system.notices)
            elif c == "6": StudentActions.view_all_staff(self.school_system.staff)
            elif c == "7": StudentActions.search_staff(self.school_system.staff)
            elif c == "8": break
            else: print("Invalid choice!")

