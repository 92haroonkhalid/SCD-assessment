from login import login
from student import Student
from result import calculate_grade
from report import generate_report

def main():
    print("=== Student Result System ===")
    username = input("Username: ")
    password = input("Password: ")
    success, role = login(username, password)
    if not success:
        print("Login failed!")
        return

    if role == "admin":
        std = Student("S001", "Ahmed Khan", "10th")
        marks = {"Math": 85, "Physics": 92, "English": 78}
        generate_report(std, marks)
    else:
        print("Student view - limited access")

if __name__ == "__main__":
    main()