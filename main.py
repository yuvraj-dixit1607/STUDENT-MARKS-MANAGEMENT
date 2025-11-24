
from operations import add_student, update_student, delete_student
from reports import view_all_students, search_student, show_class_statistics



while True:
    print("**** Student Marks Management System ****")
    print("1. Add Student")
    print("2. Update Student Marks")
    print("3. Delete Student")
    print("4. View All Students")
    print("5. Search Student by Roll Number")
    print("6. Show Class Statistics")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        update_student()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        view_all_students()
    elif choice == "5":
        search_student()
    elif choice == "6":
        show_class_statistics()
    elif choice == "7":
        print("Exiting program...")
        break
    else:
        print("Please enter a vailid choice.\n")

