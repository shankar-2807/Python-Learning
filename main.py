import getpass
from typing import List, Dict

courses: List[Dict] = [] # {id, name}
staff: List[Dict] = [] # {id, name, dept}
students: List[Dict] = [] # {roll, name, password}
notices: List[Dict] = [] # {id, title, msg}


principal_password = "admin123" # default






def prompt_nonempty(label: str) -> str:
    while True:
        val = input(label).strip()
        if val:
            return val
        print("Value cannot be empty. Try again.")




def find_by_key(data: List[Dict], key: str, value: str):
    for item in data:
        if str(item.get(key)) == str(value):
            return item
    return None



def ensure_unique(data: List[Dict], key: str, value: str) -> bool:
    return find_by_key(data, key, value) is None

def show_all(data: List[Dict], title: str):
    print(f"--- {title} ---")
    if not data:
        print("No records found.")
    else:
        for d in data:
            print(d)
    print("-------------------------")


def search_keyword(data: List[Dict], keys: List[str], keyword: str) -> List[Dict]:
    keyword = keyword.lower()
    results = []
    for item in data:
        for k in keys:
            val = str(item.get(k, "")).lower()
            if keyword in val:
                results.append(item)
                break
    return results


# Password


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

# ----- Course CRUD -----

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
    new_name = prompt_nonempty("Enter New Course Name: ")
    c["name"] = new_name
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


# ----- Staff CRUD -----


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


# ----- Student CRUD -----


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


# ----- Notice CRUD -----


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



#######################################

def student_change_password(student: Dict):
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


# Read-only views + search for Student


def student_view_all_courses():
    show_all(courses, "All Courses")




def student_search_course():
    kw = prompt_nonempty("Enter keyword (id/name): ")
    res = search_keyword(courses, ["id", "name"], kw)
    show_all(res, "Course Search Results")




def student_view_all_staff():
    show_all(staff, "All Staff")




def student_search_staff():
    kw = prompt_nonempty("Enter keyword (id/name/dept): ")
    res = search_keyword(staff, ["id", "name", "dept"], kw)
    show_all(res, "Staff Search Results")




def student_view_all_notices():
    show_all(notices, "All Notices")




def student_search_notice():
    kw = prompt_nonempty("Enter keyword (id/title/msg): ")
    res = search_keyword(notices, ["id", "title", "msg"], kw)
    show_all(res, "Notice Search Results")



########################################


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
        if ch == "1":
            principal_change_password()
        elif ch == "2":
            course_menu()
        elif ch == "3":
            staff_menu()
        elif ch == "4":
            student_admin_menu()
        elif ch == "5":
            notice_menu()
        elif ch == "6":
            break
        else:
            print("Invalid choice!")

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


def student_menu(student: Dict):
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
        elif c == "2": student_view_all_courses()
        elif c == "3": student_search_course()
        elif c == "4": student_view_all_notices()
        elif c == "5": student_search_notice()
        elif c == "6": student_view_all_staff()
        elif c == "7": student_search_staff()
        elif c == "8": break
        else: print("Invalid choice!")


#################################################

def principal_login():
    #pwd = getpass.getpass("Enter Principal Password: ")
    pwd = input("Enter Principal Password: ")
    if pwd == principal_password:
        principal_menu()
    else:
        print("Incorrect password!")




def student_login():
    roll = prompt_nonempty("Enter Roll No: ")
    st = find_by_key(students, "roll", roll)
    if not st:
        print("Student not found! Ask Principal to add your account.")
        
        return
    pwd = getpass.getpass("Enter Password: ")
    if pwd != st.get("password"):
        print("Incorrect password!")
        return
    student_menu(st)


###############################################

def main():
    while True:
        print("""Welcome to College Management System
                1. Principal Login
                2. Student Login
                3. Exit """)
        
        choice = input("Enter choice: ").strip()
        if choice == "1":
            principal_login()
        elif choice == "2":
            student_login()
        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice!")




if __name__ == "__main__":
    main()