rom data import students


def view_all_students():
    print("\n*** All Students ***")

    for student in students:
        print(f"Roll: {student['roll']}  Name: {student['name']}")
        print(f"Marks: {student['m1']}, {student['m2']}, {student['m3']}")
        print(f"Total: {student['total']}  Percent: {student['percent']}  Grade: {student['grade']}")
        print("-" * 50)
    


def search_student():
    print("\n*** Search Student ***")
    roll = input("Enter roll number to search: ")

    for student in students:
        if student["roll"] == roll:
            print(f"\nRoll: {student['roll']}  Name: {student['name']}")
            print(f"Marks: {student['m1']}, {student['m2']}, {student['m3']}")
            print(f"Total: {student['total']}  Percent: {student['percent']:.2f}  Grade: {student['grade']}\n")
            return

    print("Student not found.\n")


def show_class_statistics():
    print("\n=== Class Statistics ===")
    if not students:
        print("No students to calculate statistics.\n")
        return

    total_students = len(students)
    total_percent = 0
    topper = students[0]

    for student in students:
        total_percent += student["percent"]
        if student["total"] > topper["total"]:
            topper = student

    avg_percent = total_percent / total_students

    print(f"Total students : {total_students}")
    print(f"Average percent : {avg_percent}%")
    print(f"Topper : {topper['name']} Roll number : {topper['roll']} with {topper['percent']}%\n")
