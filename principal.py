import getpass
from helpers import prompt_nonempty, ensure_unique, find_by_key, search_keyword, show_all


courses = []
staff = []
students = []
notices = []

principal_password = "admin123"

# ---------- LOGIN FUNCTIONS ----------
def principal_login():
    global principal_password
    pwd = getpass.getpass("Enter Principal Password: ")
    if pwd == principal_password:
        print(" Login successful! Welcome Principal.")
        return True
    else:
        print("Incorrect password!")
        return False

def student_login():
    roll = prompt_nonempty("Enter Student Roll No: ")
    st = find_by_key(students, "roll", roll)
    if not st:
        print(" Student not found!")
        return None
    pwd = getpass.getpass("Enter Password: ")
    if pwd == st["password"]:
        print(f"Welcome {st['name']}!")
        return st   
    else:
        print(" Incorrect password!")
        return None

# ---------- Principal password change ----------
def principal_change_password():
    global principal_password
    old = getpass.getpass("Enter old password: ")
    if old != principal_password:
        print("Incorrect old password!")
        return
    new = getpass.getpass("Enter new password: ")
    if not new:
        print("New password cannot be empty.")
        return
    principal_password = new
    print("Password changed successfully!")

# ---------- Course CRUD ----------
def add_course():
    cid = prompt_nonempty("Enter Course ID: ")
    if not ensure_unique(courses, "id", cid):
        print("Course ID already exists!")
        return
    name = prompt_nonempty("Enter Course Name: ")
    courses.append({"id": cid, "name": name})
    print("Course added successfully!")

def update_course():
    cid = prompt_nonempty("Enter Course ID to update: ")
    c = find_by_key(courses, "id", cid)
    if not c:
        print("Course not found!")
        return
    c["name"] = prompt_nonempty("Enter New Course Name: ")
    print("Course updated!")

def delete_course():
    cid = prompt_nonempty("Enter Course ID to delete: ")
    c = find_by_key(courses, "id", cid)
    if not c:
        print("Course not found!")
        return
    courses.remove(c)
    print("Course deleted!")

def search_course():
    kw = prompt_nonempty("Enter keyword (id/name): ")
    res = search_keyword(courses, ["id", "name"], kw)
    show_all(res, "Course Search Results")

# ---------- Staff CRUD ----------
def add_staff():
    sid = prompt_nonempty("Enter Staff ID: ")
    if not ensure_unique(staff, "id", sid):
        print("Staff ID already exists!")
        return
    name = prompt_nonempty("Enter Staff Name: ")
    dept = prompt_nonempty("Enter Department: ")
    staff.append({"id": sid, "name": name, "dept": dept})
    print("Staff added successfully!")

def update_staff():
    sid = prompt_nonempty("Enter Staff ID to update: ")
    s = find_by_key(staff, "id", sid)
    if not s:
        print("Staff not found!")
        return
    s["name"] = prompt_nonempty("Enter New Staff Name: ")
    s["dept"] = prompt_nonempty("Enter New Department: ")
    print("Staff updated!")

def delete_staff():
    sid = prompt_nonempty("Enter Staff ID to delete: ")
    s = find_by_key(staff, "id", sid)
    if not s:
        print("Staff not found!")
        return
    staff.remove(s)
    print("Staff deleted!")

def search_staff():
    kw = prompt_nonempty("Enter keyword (id/name/dept): ")
    res = search_keyword(staff, ["id", "name", "dept"], kw)
    show_all(res, "Staff Search Results")

# ---------- Student CRUD ----------
def add_student():
    roll = prompt_nonempty("Enter Student Roll No: ")
    if not ensure_unique(students, "roll", roll):
        print("Student roll already exists!")
        return
    name = prompt_nonempty("Enter Student Name: ")
    pwd = getpass.getpass("Set Student Password: ") or "1234"
    students.append({"roll": roll, "name": name, "password": pwd})
    print("Student added successfully! (default password set)")

def update_student():
    roll = prompt_nonempty("Enter Student Roll No to update: ")
    st = find_by_key(students, "roll", roll)
    if not st:
        print("Student not found!")
        return
    st["name"] = prompt_nonempty("Enter New Student Name: ")
    print("Student updated!")

def delete_student():
    roll = prompt_nonempty("Enter Student Roll No to delete: ")
    st = find_by_key(students, "roll", roll)
    if not st:
        print("Student not found!")
        return
    students.remove(st)
    print("Student deleted!")

def search_student():
    kw = prompt_nonempty("Enter keyword (roll/name): ")
    res = search_keyword(students, ["roll", "name"], kw)
    show_all(res, "Student Search Results")

# ---------- Notice CRUD ----------
def add_notice():
    nid = prompt_nonempty("Enter Notice ID: ")
    if not ensure_unique(notices, "id", nid):
        print("Notice ID already exists!")
        return
    title = prompt_nonempty("Enter Notice Title: ")
    msg = prompt_nonempty("Enter Notice Message: ")
    notices.append({"id": nid, "title": title, "msg": msg})
    print("Notice added successfully!")

def update_notice():
    nid = prompt_nonempty("Enter Notice ID to update: ")
    n = find_by_key(notices, "id", nid)
    if not n:
        print("Notice not found!")
        return
    n["title"] = prompt_nonempty("Enter New Title: ")
    n["msg"] = prompt_nonempty("Enter New Message: ")
    print("Notice updated!")

def delete_notice():
    nid = prompt_nonempty("Enter Notice ID to delete: ")
    n = find_by_key(notices, "id", nid)
    if not n:
        print("Notice not found!")
        return
    notices.remove(n)
    print("Notice deleted!")

def search_notice():
    kw = prompt_nonempty("Enter keyword (id/title/msg): ")
    res = search_keyword(notices, ["id", "title", "msg"], kw)
    show_all(res, "Notice Search Results")


