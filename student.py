import getpass
from helpers import Helper

class StudentActions:
    @staticmethod
    def change_password(student):
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

    @staticmethod
    def view_all_courses(courses):
        Helper.show_all(courses, "All Courses")

    @staticmethod
    def search_course(courses):
        kw = Helper.prompt_nonempty("Enter keyword (id/name): ")
        res = Helper.search_keyword(courses, ["id", "name"], kw)
        Helper.show_all(res, "Course Search Results")

    @staticmethod
    def view_all_staff(staff):
        Helper.show_all(staff, "All Staff")

    @staticmethod
    def search_staff(staff):
        kw = Helper.prompt_nonempty("Enter keyword (id/name/dept): ")
        res = Helper.search_keyword(staff, ["id", "name", "dept"], kw)
        Helper.show_all(res, "Staff Search Results")

    @staticmethod
    def view_all_notices(notices):
        Helper.show_all(notices, "All Notices")

    @staticmethod
    def search_notice(notices):
        kw = Helper.prompt_nonempty("Enter keyword (id/title/msg): ")
        res = Helper.search_keyword(notices, ["id", "title", "msg"], kw)
        Helper.show_all(res, "Notice Search Results")

