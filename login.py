from principal import Principal
from student import Student

class Login:
    def __init__(self):
        self.credentials_file = "credentials.txt"

    def start(self):
        while True:
            print("\n1. Principal Login")
            print("2. Student Login")
            print("3. Exit")
            choice = input("Choose: ")

            if choice == '1':
                self.principal_login()
            elif choice == '2':
                self.student_login()
            elif choice == '3':
                print("Exiting...")
                break
            else:
                print("Invalid choice!")

    def principal_login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        try:
            with open(self.credentials_file, "r") as f:
                for line in f:
                    u, p, role, *_ = line.strip().split("|")
                    if u == username and p == password and role == "principal":
                        print("Login successful!")
                        Principal(username).menu()
                        return
            print("Login failed: Invalid username or password")
        except FileNotFoundError:
            print("Error: credentials.txt not found")

    def student_login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        try:
            with open(self.credentials_file, "r") as f:
                for line in f:
                    parts = line.strip().split("|")
                    if len(parts) >= 4:
                        u, p, role, sid = parts
                        if u == username and p == password and role == "student":
                            print("Login successful!")
                            Student(username, sid).menu()
                            return
            print("Login failed: Invalid username or password")
        except FileNotFoundError:
            print("Error: credentials.txt not found")




