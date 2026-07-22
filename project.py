students = []

def load_student():

    file = open("students.txt","r")

    for line in file:

        name, age, marks, course = line.strip().split(",")

        student = {
            "name": name,
            "age": int(age),
            "marks": int(marks),
            "course": course
        }

        students.append(student)

    file.close()


def save_students():

    file = open("students.txt", "w")

    for student in students:

        file.write(
            f"{student['name']},{student['age']},{student['marks']},{student['course']}\n"
        )

    file.close()


def add_student():

    name = input("enter Name: ")
    age = int(input("enter Age: "))
    marks = int(input("enter Marks: "))
    course = input("enter Course: ")

    student = {
        "name": name,
        "age": age,
        "marks": marks,
        "course": course
    }

    students.append(student)

    file = open("students.txt","a")

    file.write(f"{name},{age},{marks},{course}\n")

    file.close()

    print("Student Added Successfully")


def view_students():

    for student in students:
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Marks:", student["marks"])
        print("Course:", student["course"])
        print("----------------")


def search_student():

    search_name = input("Enter student name: ")

    for student in students:

        if student["name"] == search_name:

            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Marks:", student["marks"])
            print("Course:", student["course"])

            return

    print("Student Not Found")


def delete_student():

    delete_name = input("Enter student name to delete: ")

    for student in students:

        if student["name"] == delete_name:

            students.remove(student)

            save_students()

            print("Student Deleted Successfully")

            return

    print("Student Not Found")


load_student()

while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank You")
        break

    else:
        print("Invalid Choice")