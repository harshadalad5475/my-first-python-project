students = []

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")

        student = {
            "Name": name,
            "Roll": roll
        }
        students.append(student)
        print("Student added successfully! ")

    elif choice == "2":
        print("\nStudent List")

        if len(students) == 0:
            print("No students found. ")
        else:
            for student in students:
                print("Name:", student["Nmae"])
                print("Roll:", student["Roll"])
                print("--------------------")

    elif choice == "3":
        print("Thank you! ")
        break

    else:
        print("Invalid choice! ")
