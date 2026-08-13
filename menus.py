from principal import *
from student import *

def principal_menu():
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
        if ch == "1": principal_change_password()
        elif ch == "2": course_menu()
        elif ch == "3": staff_menu()
        elif ch == "4": student_admin_menu()
        elif ch == "5": notice_menu()
        elif ch == "6": break
        else: print("Invalid choice!")

def course_menu():
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
        if c == "1": add_course()
        elif c == "2": update_course()
        elif c == "3": delete_course()
        elif c == "4": show_all(courses, "Courses")
        elif c == "5": search_course()
        elif c == "6": break
        else: print("Invalid choice!")

def staff_menu():
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
        if c == "1": add_staff()
        elif c == "2": update_staff()
        elif c == "3": delete_staff()
        elif c == "4": show_all(staff, "Staff")
        elif c == "5": search_staff()
        elif c == "6": break
        else: print("Invalid choice!")

def student_admin_menu():
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
        if c == "1": add_student()
        elif c == "2": update_student()
        elif c == "3": delete_student()
        elif c == "4": show_all(students, "Students")
        elif c == "5": search_student()
        elif c == "6": break
        else: print("Invalid choice!")

def notice_menu():
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
        if c == "1": add_notice()
        elif c == "2": update_notice()
        elif c == "3": delete_notice()
        elif c == "4": show_all(notices, "Notices")
        elif c == "5": search_notice()
        elif c == "6": break
        else: print("Invalid choice!")

def student_menu(student):
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
        if c == "1": student_change_password(student)
        elif c == "2": student_view_all_courses(courses)
        elif c == "3": student_search_course(courses)
        elif c == "4": student_view_all_notices(notices)
        elif c == "5": student_search_notice(notices)
        elif c == "6": student_view_all_staff(staff)
        elif c == "7": student_search_staff(staff)
        elif c == "8": break
        else: print("Invalid choice!")

