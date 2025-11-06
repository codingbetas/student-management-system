import database
import functions

database.connect()

def menu():
    while True:
        print("\n=== Student Management System ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by ID")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Name: ")
            age = int(input("Age: "))
            course = input("Course: ")
            grade = input("Grade: ")
            functions.insert(name, age, course, grade)

        # elif choice == '2':
        #     for row in functions.view():
        #         print(row)

        elif choice == '2':
         students = functions.view()
         print("\n{:<8} {:<20} {:<16} {:<26} {:<17}".format("ID", "Name", "Age", "Course", "Grade"))
         print("-" * 60)
         for s in students:
           print("{:<8} {:<20} {:<16} {:<26} {:<17}".format(s[0], s[1], s[2], s[3], s[4]))



        elif choice == '3':
            id = int(input("Enter student ID: "))
            student = functions.search(id)
            print(student if student else "Student not found")

        elif choice == '4':
            id = int(input("ID to update: "))
            name = input("New Name: ")
            age = int(input("New Age: "))
            course = input("New Course: ")
            grade = input("New Grade: ")
            functions.update(id, name, age, course, grade)

        elif choice == '5':
            id = int(input("ID to delete: "))
            functions.delete(id)

        elif choice == '6':
            break

        else:
            print("Invalid choice. Try again.")

menu()
