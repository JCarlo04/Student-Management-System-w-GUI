def add_student(student_data, name, age, idnum, email, phone):
    with open("studentlist.txt", "a") as f:
        student_list = f"{name},{age},{idnum},{email},{phone}\n"
        f.write(student_list)
