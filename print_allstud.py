def printAllStudents():
    """Prints all students to the console for debugging or testing."""
    try:
        with open("studentlist.txt", "r") as f:
            students = f.readlines()

            if not students:
                print("No students in the list.")
            else:
                print("=== All Students ===")
                for student in students:
                    details = student.strip().split(",")
                    print(f'Name: {details[0]}, Age: {details[1]}, ID: {details[2]}, Email: {details[3]}, Phone: {details[4]}')
                print("====================")
    except FileNotFoundError:
        print("No student data found.")
