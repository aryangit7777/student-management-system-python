import json

print("Welcome to the Student Management System!")
print ("-----------------------------------------")




def save_students_to_file(students, filename="students.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(students, f, indent=4)


def load_students_from_file(filename="students.json"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


students = load_students_from_file()
print(f"Loaded {len(students)} existing student(s).")

def add_students():
   
    try:
        no_of_students = int(input("Enter the number of students you want to add: "))
    except ValueError:
        print("Invalid number. Using 0.")
        no_of_students = 0

    for i in range(no_of_students):
        name = input(f"Enter the name of student #{i+1}: ").strip()
        while not name:
            name = input("Please enter a valid name: ").strip()

        while True:
            try:
                age = int(input(f"Enter the age of {name}: "))
                break
            except ValueError:
                print("Please enter a valid number for age.")

        while True:
            try:
                marks = int(input(f"Enter the marks for {name}: "))
                break
            except ValueError:
                print("Please enter a valid number for marks.")

        students.append({
            "name": name,
            "age": age,
            "marks": marks,
        })

    print(f"{no_of_students} student(s) added successfully.")


def print_students():
    
    if not students:
        print("No students to display.")
        return

    print("\nStudent list:")
    for s in students:
        marks_text = f", marks {s['marks']}" if "marks" in s else ""
        print(f"- {s['name']} is {s['age']} years old{marks_text}")


def search_student():

    if not students:
        print("No students to search.")
        return

    search_name = input("\nEnter the name of the student to search: ").strip()
    for student in students:
        if student["name"].lower() == search_name.lower():
            print(f"{student['name']} is in the student list (age {student['age']}).")
            return

    print(f"{search_name} is not in the student list.")


def update_student_marks():

    student_name = input("Enter the name of the student to update marks for: ").strip()
    for student in students:
        if student["name"].lower() == student_name.lower():
            while True:
                try:
                    marks = int(input(f"Enter the new marks for {student['name']}: "))
                    break
                except ValueError:
                    print("Please enter a valid number for marks.")

            student["marks"] = marks
            print(f"Marks for {student['name']} have been updated to {marks}.")
            return

    print(f"{student_name} is not in the student list. Cannot update marks.")


def delete_student():

    student_name = input("Enter the name of the student to delete: ").strip()
    for i, student in enumerate(students):
        if student["name"].lower() == student_name.lower():
            del students[i]
            print(f"{student_name} has been deleted from the student list.")
            return

    print(f"{student_name} is not in the student list. Cannot delete.")

while True:
    print("\nmenu:")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Exit")
    Choice = input("Enter your choice (1-6): ").strip()

    if Choice == "1":
        add_students()
        save_students_to_file(students)
    elif Choice == "2":
        print_students()
    elif Choice == "3":
        search_student()
    elif Choice == "4":
        update_student_marks()
        save_students_to_file(students)
    elif Choice == "5":
        delete_student()
        save_students_to_file(students)
    elif Choice == "6":
        print("Exiting the Student Management System. Goodbye!")
        save_students_to_file(students)
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")

print("\nUpdated student list:")
print_students()
save_students_to_file(students)

