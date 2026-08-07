import getpass
from helpers import Helper

class SchoolSystem:
    def __init__(self):
        self.courses = []
        self.staff = []
        self.students = []
        self.notices = []
        self.principal_password = "admin123"

    # ---------- LOGIN ----------
    def principal_login(self):
        pwd = getpass.getpass("Enter Principal Password: ")
        if pwd == self.principal_password:
            print("Login successful! Welcome Principal.")
            return True
        else:
            print("Incorrect password!")
            return False

    def student_login(self):
        roll = Helper.prompt_nonempty("Enter Student Roll No: ")
        st = Helper.find_by_key(self.students, "roll", roll)
        if not st:
            print("Student not found!")
            return None
        pwd = getpass.getpass("Enter Password: ")
        if pwd == st["password"]:
            print(f"Welcome {st['name']}!")
            return st
        else:
            print("Incorrect password!")
            return None

    # ---------- Principal password ----------
    def principal_change_password(self):
        old = getpass.getpass("Enter old password: ")
        if old != self.principal_password:
            print("Incorrect old password!")
            return
        new = getpass.getpass("Enter new password: ")
        if not new:
            print("New password cannot be empty.")
            return
        self.principal_password = new
        print("Password changed successfully!")

    # ---------- Course CRUD ----------
    def add_course(self):
        cid = Helper.prompt_nonempty("Enter Course ID: ")
        if not Helper.ensure_unique(self.courses, "id", cid):
            print("Course ID already exists!")
            return
        name = Helper.prompt_nonempty("Enter Course Name: ")
        self.courses.append({"id": cid, "name": name})
        print("Course added successfully!")

    def update_course(self):
        cid = Helper.prompt_nonempty("Enter Course ID to update: ")
        c = Helper.find_by_key(self.courses, "id", cid)
        if not c:
            print("Course not found!")
            return
        c["name"] = Helper.prompt_nonempty("Enter New Course Name: ")
        print("Course updated!")

    def delete_course(self):
        cid = Helper.prompt_nonempty("Enter Course ID to delete: ")
        c = Helper.find_by_key(self.courses, "id", cid)
        if not c:
            print("Course not found!")
            return
        self.courses.remove(c)
        print("Course deleted!")

    def search_course(self):
        kw = Helper.prompt_nonempty("Enter keyword (id/name): ")
        res = Helper.search_keyword(self.courses, ["id", "name"], kw)
        Helper.show_all(res, "Course Search Results")

    # ---------- Staff CRUD ----------
    def add_staff(self):
        sid = Helper.prompt_nonempty("Enter Staff ID: ")
        if not Helper.ensure_unique(self.staff, "id", sid):
            print("Staff ID already exists!")
            return
        name = Helper.prompt_nonempty("Enter Staff Name: ")
        dept = Helper.prompt_nonempty("Enter Department: ")
        self.staff.append({"id": sid, "name": name, "dept": dept})
        print("Staff added successfully!")

    def update_staff(self):
        sid = Helper.prompt_nonempty("Enter Staff ID to update: ")
        s = Helper.find_by_key(self.staff, "id", sid)
        if not s:
            print("Staff not found!")
            return
        s["name"] = Helper.prompt_nonempty("Enter New Staff Name: ")
        s["dept"] = Helper.prompt_nonempty("Enter New Department: ")
        print("Staff updated!")

    def delete_staff(self):
        sid = Helper.prompt_nonempty("Enter Staff ID to delete: ")
        s = Helper.find_by_key(self.staff, "id", sid)
        if not s:
            print("Staff not found!")
            return
        self.staff.remove(s)
        print("Staff deleted!")

    def search_staff(self):
        kw = Helper.prompt_nonempty("Enter keyword (id/name/dept): ")
        res = Helper.search_keyword(self.staff, ["id", "name", "dept"], kw)
        Helper.show_all(res, "Staff Search Results")

    # ---------- Student CRUD ----------
    def add_student(self):
        roll = Helper.prompt_nonempty("Enter Student Roll No: ")
        if not Helper.ensure_unique(self.students, "roll", roll):
            print("Student roll already exists!")
            return
        name = Helper.prompt_nonempty("Enter Student Name: ")
        pwd = getpass.getpass("Set Student Password: ") or "1234"
        self.students.append({"roll": roll, "name": name, "password": pwd})
        print("Student added successfully! (default password set)")

    def update_student(self):
        roll = Helper.prompt_nonempty("Enter Student Roll No to update: ")
        st = Helper.find_by_key(self.students, "roll", roll)
        if not st:
            print("Student not found!")
            return
        st["name"] = Helper.prompt_nonempty("Enter New Student Name: ")
        print("Student updated!")

    def delete_student(self):
        roll = Helper.prompt_nonempty("Enter Student Roll No to delete: ")
        st = Helper.find_by_key(self.students, "roll", roll)
        if not st:
            print("Student not found!")
            return
        self.students.remove(st)
        print("Student deleted!")

    def search_student(self):
        kw = Helper.prompt_nonempty("Enter keyword (roll/name): ")
        res = Helper.search_keyword(self.students, ["roll", "name"], kw)
        Helper.show_all(res, "Student Search Results")

    # ---------- Notice CRUD ----------
    def add_notice(self):
        nid = Helper.prompt_nonempty("Enter Notice ID: ")
        if not Helper.ensure_unique(self.notices, "id", nid):
            print("Notice ID already exists!")
            return
        title = Helper.prompt_nonempty("Enter Notice Title: ")
        msg = Helper.prompt_nonempty("Enter Notice Message: ")
        self.notices.append({"id": nid, "title": title, "msg": msg})
        print("Notice added successfully!")

    def update_notice(self):
        nid = Helper.prompt_nonempty("Enter Notice ID to update: ")
        n = Helper.find_by_key(self.notices, "id", nid)
        if not n:
            print("Notice not found!")
            return
        n["title"] = Helper.prompt_nonempty("Enter New Title: ")
        n["msg"] = Helper.prompt_nonempty("Enter New Message: ")
        print("Notice updated!")

    def delete_notice(self):
        nid = Helper.prompt_nonempty("Enter Notice ID to delete: ")
        n = Helper.find_by_key(self.notices, "id", nid)
        if not n:
            print("Notice not found!")
            return
        self.notices.remove(n)
        print("Notice deleted!")

    def search_notice(self):
        kw = Helper.prompt_nonempty("Enter keyword (id/title/msg): ")
        res = Helper.search_keyword(self.notices, ["id", "title", "msg"], kw)
        Helper.show_all(res, "Notice Search Results")

        