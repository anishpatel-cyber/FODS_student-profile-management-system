#  IMPORTS 
from colorama import Fore, Style, init
import matplotlib.pyplot as plt

# ===== OOP CLASSES =====

class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def display(self):
        print(f"Name: {self.name}, Role: {self.role}")


class Student(User):
    def __init__(self, name, role="student"):
        super().__init__(name, role)

    def dashboard(self):
        print("Welcome Student!")


class Admin(User):
    def __init__(self, name, role="admin"):
        super().__init__(name, role)

    def dashboard(self):
        print("Welcome Admin!")


init()

#  UI FUNCTIONS 
def title(text):
    print(Fore.CYAN + "\n" + "="*45)
    print(text.center(45))
    print("="*45 + Style.RESET_ALL)


def menu(text):
    print(Fore.YELLOW + text + Style.RESET_ALL)


def success(text):
    print(Fore.GREEN + text + Style.RESET_ALL)


def error(text):
    print(Fore.RED + text + Style.RESET_ALL)


#  LOGIN 
def login():
    while True:
        title("STUDENT MANAGEMENT SYSTEM")

        username = input("👤 Username: ")
        password = input("🔒 Password: ")

        try:
            with open("passwords.txt", "r") as file:
                for line in file:
                    user, pwd = line.strip().split(",")

                    if username == user and password == pwd:
                        success("✔ Login successful!\n")
                        return username

            error("❌ Invalid login! Try again.\n")

        except FileNotFoundError:
            error("⚠ File not found!")
            return None
        

#  GET ROLE 
def get_role(username):
    with open("users.txt", "r") as file:
        for line in file:
            id, name, role = line.strip().split(",")
            if name == username:
                return role


#  ADMIN FUNCTIONS 
def add_user():
    name = input("Enter name: ")
    role = input("Enter role (admin/student): ")
    password = input("Enter password: ")

    with open("users.txt", "a") as file:
        file.write(f"0,{name},{role}\n")

    with open("passwords.txt", "a") as file:
        file.write(f"{name},{password}\n")

    success(" User added successfully!")
    input("\nPress Enter to continue...")


def view_users():
    title("USERS LIST")
    with open("users.txt", "r") as file:
        for line in file:
            print(line.strip())

    input("\nPress Enter to continue...")


def delete_user():
    name = input("Enter username to delete: ")

    # users.txt
    lines = []
    with open("users.txt", "r") as file:
        for line in file:
            if name not in line:
                lines.append(line)

    with open("users.txt", "w") as file:
        file.writelines(lines)

    # passwords.txt
    lines = []
    with open("passwords.txt", "r") as file:
        for line in file:
            if name not in line:
                lines.append(line)

    with open("passwords.txt", "w") as file:
        file.writelines(lines)

    success(" User deleted!")
    input("\nPress Enter to continue...")


def add_grades():
    name = input("Enter student name: ")
    marks = input("Enter 5 marks (comma separated): ")

    with open("grades.txt", "a") as file:
        file.write(f"{name},{marks}\n")

    success(" Grades added!")
    input("\nPress Enter to continue...")


def add_eca():
    name = input("Enter student name: ")
    activity = input("Enter ECA: ")

    with open("eca.txt", "a") as file:
        file.write(f"{name},{activity}\n")

    success(" ECA added!")
    input("\nPress Enter to continue...")



# Calculate Average function
def calculate_average():
    title("AVERAGE MARKS")

    try:
        with open("grades.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                name = data[0]
                marks = list(map(int, data[1:]))
                avg = sum(marks) / len(marks)
                print(f"{name}: {avg:.2f}")

    except:
        error("⚠ Error reading grades file!")

    input("\nPress Enter to continue...")


#  ANALYTICS 
def grade_trends():
    title("GRADE TRENDS")

    with open("grades.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            name = data[0]
            marks = list(map(int, data[1:]))

            plt.plot(marks, marker='o', label=name)

    plt.title("Grade Trends")
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.legend()
    plt.show()


def eca_impact():
    title("ECA IMPACT")

    eca_students = []

    with open("eca.txt", "r") as file:
        for line in file:
            name, _ = line.strip().split(",")
            eca_students.append(name)

    with open("grades.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            name = data[0]
            marks = list(map(int, data[1:]))
            avg = sum(marks) / len(marks)

            if name in eca_students:
                print(f"{name} (ECA): {avg:.2f}")
            else:
                print(f"{name} (No ECA): {avg:.2f}")

    input("\nPress Enter to continue...")


#Performance Alert

def performance_alert():
    try:
        threshold = int(input("Enter minimum average: "))
    except ValueError:
        error("⚠ Please enter a valid number!")
        return

    title("PERFORMANCE ALERT")

    try:
        with open("grades.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                name = data[0]
                marks = list(map(int, data[1:]))
                avg = sum(marks) / len(marks)

                if avg < threshold:
                    print(f"{name} → Needs Improvement!")

    except:
        error("⚠ Error reading file!")

    input("\nPress Enter to continue...")


#  STUDENT FUNCTIONS 
def view_profile(username):
    title("PROFILE")

    with open("users.txt", "r") as file:
        for line in file:
            id, name, role = line.strip().split(",")
            if name == username:
                print(f"Name: {name}")
                print(f"Role: {role}")

    input("\nPress Enter to continue...")


def view_grades(username):
    title("GRADES")

    with open("grades.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] == username:
                print("Marks:", data[1:])

    input("\nPress Enter to continue...")


def view_eca(username):
    title("ECA")

    with open("eca.txt", "r") as file:
        for line in file:
            name, eca = line.strip().split(",")
            if name == username:
                print("Activity:", eca)

    input("\nPress Enter to continue...")

# Update Profile

def update_profile(username):
    new_name = input("Enter new name: ")

    # ===== UPDATE users.txt =====
    lines = []
    with open("users.txt", "r") as file:
        for line in file:
            id, name, role = line.strip().split(",")
            if name == username:
                lines.append(f"{id},{new_name},{role}\n")
            else:
                lines.append(line)

    with open("users.txt", "w") as file:
        file.writelines(lines)

    # ===== UPDATE passwords.txt =====
    lines = []
    with open("passwords.txt", "r") as file:
        for line in file:
            user, pwd = line.strip().split(",")
            if user == username:
                lines.append(f"{new_name},{pwd}\n")
            else:
                lines.append(line)

    with open("passwords.txt", "w") as file:
        file.writelines(lines)

    # ===== UPDATE grades.txt =====
    lines = []
    with open("grades.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] == username:
                lines.append(",".join([new_name] + data[1:]) + "\n")
            else:
                lines.append(line)

    with open("grades.txt", "w") as file:
        file.writelines(lines)

    # ===== UPDATE eca.txt =====
    lines = []
    with open("eca.txt", "r") as file:
        for line in file:
            name, eca = line.strip().split(",")
            if name == username:
                lines.append(f"{new_name},{eca}\n")
            else:
                lines.append(line)

    with open("eca.txt", "w") as file:
        file.writelines(lines)

    success("✔ Profile updated!")

    return new_name   # VERY IMPORTANT

#  ADMIN MENUS 
def admin_menu():
    while True:
        title("ADMIN DASHBOARD")

        menu("1. Add User")
        menu("2. View Users")
        menu("3. Delete User")
        menu("4. Add Grades")
        menu("5. Add ECA")
        menu("6. Average Marks")
        menu("7. Grade Trends")
        menu("8. ECA Impact")
        menu("9. Performance Alert")
        menu("10. Logout")

        choice = input("\n👉 Enter choice: ")

        if choice == "1":
            add_user()
        elif choice == "2":
            view_users()
        elif choice == "3":
            delete_user()
        elif choice == "4":
            add_grades()
        elif choice == "5":
            add_eca()
        elif choice == "6":
            calculate_average()
        elif choice == "7":
            grade_trends()
        elif choice == "8":
            eca_impact()
        elif choice == "9":
            performance_alert()
        elif choice == "10":
            success("Logged out!")
            break
        else:
            error("Invalid choice")

# STUDENT MENU

def student_menu(username):
    while True:
        title(f"STUDENT DASHBOARD ({username})")

        menu("1. View Profile")
        menu("2. View Grades")
        menu("3. View ECA")
        menu("4. Update Profile")
        menu("5. Logout")

        choice = input("\n👉 Enter choice: ")

        if choice == "1":
            view_profile(username)
        elif choice == "2":
            view_grades(username)
        elif choice == "3":
            view_eca(username)
        elif choice == "4":
            username = update_profile(username)
        elif choice == "5":
            success("Logged out!")
            break
        else:
            error("Invalid choice")


#  MAIN 
def main():
    username = login()
    role = get_role(username)

    if role == "admin":
        user = Admin(username)
        user.dashboard()
        admin_menu()
    else:
        user = Student(username)
        user.dashboard()
        student_menu(username)


#  RUN 
main()