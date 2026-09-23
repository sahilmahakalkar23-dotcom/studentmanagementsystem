# Main dictionary to store student data
students = {}

def calculate_result(marks):
    total = sum(marks)
    percentage = total / len(marks)
    
    if percentage >= 90:
        grade = "S"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"
        
    return total, percentage, grade


def add_student():
    roll_no = input("Enter roll number: ")
    if roll_no in students:
        print("Student already exists!")
        return

    name = input("Enter student name: ")
    marks_list = []
    subjects = ["hindi", "maths", "english", "physics", "chemistry"]
    
    for subject in subjects:
        mark = int(input(f"Enter marks for {subject}: "))
        marks_list.append(mark)
        
    total, percentage, grade = calculate_result(marks_list)
    
    students[roll_no] = {
        "name": name,
        "marks": marks_list,
        "total": total,
        "percentage": percentage,
        "grade": grade,
    }
    print("Student added successfully!")


def display_students():
    if not students:
        print("No student record found.")
        return

    for roll_no, data in students.items():
        print(f"\nRoll Number: {roll_no}")
        print(f"Name: {data['name']}")
        print(f"Marks: {data['marks']}")
        print(f"Total: {data['total']}")
        print(f"Percentage: {data['percentage']:.2f}%")
        print(f"Grade: {data['grade']}")


def search_student():
    roll_no = input("Enter student roll number to search: ")
    if roll_no in students:
        data = students[roll_no]
        print("\n--- Student Found ---")
        print(f"Roll Number: {roll_no}")
        print(f"Name: {data['name']}")
        print(f"Marks: {data['marks']}")
        print(f"Total: {data['total']}")
        print(f"Percentage: {data['percentage']:.2f}%")
        print(f"Grade: {data['grade']}")
    else:
        print("Student not found.")


def update_student():
    roll_no = input("Enter roll number to update: ")
    if roll_no not in students:
        print("Student not found.")
        return

    name = input("Enter new name: ")
    marks_list = []
    subjects = ["hindi", "maths", "english", "physics", "chemistry"]
    
    for subject in subjects:
        mark = int(input(f"Enter new marks for {subject}: "))
        marks_list.append(mark)
        
    total, percentage, grade = calculate_result(marks_list)
    
    students[roll_no] = {
        "name": name,
        "marks": marks_list,
        "total": total,
        "percentage": percentage,
        "grade": grade,
    }
    print("Student updated successfully!")


def delete_student():
    roll_no = input("Enter student roll number to delete: ")
    if roll_no in students:
        del students[roll_no]
        print("Student deleted successfully!")
    else:
        print("Student not found.")


# Main Menu Loop
while True:
    print("\n=== Student Result Management System ===")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Thank you for using the system!")
        break
    else:
        print("Invalid choice! Please select between 1 and 6.")