from data import students


def calculate_total_and_grade(m1, m2, m3):
    total = m1 + m2 + m3
    percent = round(total / 3,2)

    if percent >= 90:
        grade = "A+"
    elif percent >= 80:
        grade = "A"
    elif percent >= 70:
        grade = "B"
    elif percent >= 60:
        grade = "C"
    elif percent >= 50:
        grade = "D"
    else:
        grade = "F"

    return total, percent, grade


def add_student():
    print("\n*** Add Student ***")
    roll = input("Enter roll number: ")

    # checks for duplicate roll number
    for student in students:
        if student["roll"] == roll:
            print("Student with this roll number already exists.\n")
            return

    name = input("Enter name: ")


    m1 = int(input("Marks in Subject 1: "))
    m2 = int(input("Marks in Subject 2: "))
    m3 = int(input("Marks in Subject 3: "))
  

    total, percent, grade = calculate_total_and_grade(m1, m2, m3)

    student = {
        "roll": roll,
        "name": name,
        "m1": m1,
        "m2": m2,
        "m3": m3,
        "total": total,
        "percent": percent,
        "grade": grade,
    }

    students.append(student)
    print("Student added successfully!\n")


def update_student():
    print("\n*** Update Student Marks ***")
    roll = input("Enter roll number to update: ")

    for student in students:
        if student["roll"] == roll:
            print(f"Current marks: {student['m1']}, {student['m2']}, {student['m3']}")
            
            m1 = int(input("New marks in Subject 1: "))
            m2 = int(input("New marks in Subject 2: "))
            m3 = int(input("New marks in Subject 3: "))
            
            

            total, percent, grade = calculate_total_and_grade(m1, m2, m3)
            student["m1"] = m1
            student["m2"] = m2
            student["m3"] = m3
            student["total"] = total
            student["percent"] = percent
            student["grade"] = grade
            print("Student updated!\n")
            return

    print("Student not found.")


def delete_student():
    print("\n*** Delete Student ***")
    roll = input("Enter roll number to delete: ")

    for student in students:
        if student["roll"] == roll:
            students.pop(student)
            print("Student deleted.\n")

    print("Student not found.\n")
