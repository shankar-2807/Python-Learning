import getpass
from helpers import prompt_nonempty, search_keyword, show_all

def student_change_password(student):
    old = getpass.getpass("Enter old password: ")
    if old != student.get("password"):
        print("Incorrect old password!")
        return
    new = getpass.getpass("Enter new password: ")
    if not new:
        print("New password cannot be empty.")
        return
    student["password"] = new
    print("Password changed successfully!")

def student_view_all_courses(courses):
    show_all(courses, "All Courses")

def student_search_course(courses):
    kw = prompt_nonempty("Enter keyword (id/name): ")
    res = search_keyword(courses, ["id", "name"], kw)
    show_all(res, "Course Search Results")

def student_view_all_staff(staff):
    show_all(staff, "All Staff")

def student_search_staff(staff):
    kw = prompt_nonempty("Enter keyword (id/name/dept): ")
    res = search_keyword(staff, ["id", "name", "dept"], kw)
    show_all(res, "Staff Search Results")

def student_view_all_notices(notices):
    show_all(notices, "All Notices")

def student_search_notice(notices):
    kw = prompt_nonempty("Enter keyword (id/title/msg): ")
    res = search_keyword(notices, ["id", "title", "msg"], kw)
    show_all(res, "Notice Search Results")

    