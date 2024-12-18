from tkinter import *
import tkinter.scrolledtext as st
from student import StudentInfo
from add_student import add_student
from search_student import SearchStudent
from print_allstud import *

stu = StudentInfo()
stu.read()
search = SearchStudent(stu)

win = Tk()
win.geometry("1200x800+{}+{}".format(win.winfo_screenwidth()//2-600, win.winfo_screenheight()//2-400))
win.title("Stardew Management System")

bg_color = "#a8d5e2"
frame_color = "#d9bfa8"
button_color = "#b7835a" 
font_color = "#3a2e23"
font_family = "Comic Sans MS"

login_frame = Frame(win, bg=bg_color)
login_frame.pack(fill="both", expand=True)

main_menu = Frame(win, borderwidth=1, bg=frame_color, relief="sunken")
float_frame = Frame(win, borderwidth=1, bg=bg_color)

dynamic_frame = Frame(float_frame, bg=bg_color, padx=20, pady=20)
dynamic_frame.place(relx=0.5, rely=0.5, anchor="center")

def logout():
    login_entry.delete(0, END)
    main_menu.pack_forget()
    float_frame.pack_forget()
    login_frame.pack(fill="both", expand=True)

def view_your():
    for widget in dynamic_frame.winfo_children():
        widget.destroy()

    Label(dynamic_frame, text="Your Information", font=(font_family, 24), fg=font_color, bg=bg_color).pack(pady=10)
    info_labels = [
        f"Name: {stu.getName()}",
        f"Age: {stu.getAge()}",
        f"ID: {stu.getIDNum()}",
        f"Email: {stu.getEmail()}",
        f"Phone: {stu.getPhone()}"
    ]
    for info in info_labels:
        Label(dynamic_frame, text=info, font=(font_family, 18), fg=font_color, bg=bg_color).pack()

def search_stud():
    for widget in dynamic_frame.winfo_children():
        widget.destroy()

    def perform_search():
        student_id = search_entry.get()
        for student in stu.allstudents:
            if student.getIDNum() == student_id:
                result_label.config(text=str(student))
                return
        result_label.config(text="Student not found.")

    Label(dynamic_frame, text="Search Student by ID", font=(font_family, 24), fg=font_color, bg=bg_color).pack(pady=10)
    search_entry = Entry(dynamic_frame, font=(font_family, 18))
    search_entry.pack()
    Button(dynamic_frame, text="Search", font=(font_family, 18), bg=button_color, fg="white", command=perform_search).pack(pady=10)
    result_label = Label(dynamic_frame, text="", font=(font_family, 18), fg=font_color, bg=bg_color)
    result_label.pack()

def add_stud():
    for widget in dynamic_frame.winfo_children():
        widget.destroy()
        
    def clear_error_label(event, error_label):
        error_label.config(text="")

    def perform_add():
        name = name_entry.get().strip()
        age = age_entry.get().strip()
        idnum = id_entry.get().strip()
        email = email_entry.get().strip()
        phone = phone_entry.get().strip()

        errors = False 

        if not name:
            name_error.config(text="Name is required!")
            errors = True
        if not age:
            age_error.config(text="Age is required!")
            errors = True
        if not idnum:
            id_error.config(text="ID Number is required!")
            errors = True
        if not email:
            email_error.config(text="Email is required!")
            errors = True
        if not phone:
            phone_error.config(text="Phone is required!")
            errors = True

        if errors:
            return

        add_student(None, name, age, idnum, email, phone)

        new_student = StudentInfo()
        new_student.setFirstName(name)
        new_student.setAge(age)
        new_student.setIDNum(idnum)
        new_student.setEmail(email)
        new_student.setPhoneNumber(phone)
        stu.allstudents.append(new_student)

        Label(dynamic_frame, text=f"Student {name} added successfully!", font=(font_family, 18), fg="green", bg=bg_color).pack()

    Label(dynamic_frame, text="Add New Student", font=(font_family, 24), fg=font_color, bg=bg_color).pack(pady=10)

    fields = ["Name", "Age", "ID Number", "Email", "Phone"]
    entries = []
    error_labels = []

    for field in fields:
        Label(dynamic_frame, text=field, font=(font_family, 18), fg=font_color, bg=bg_color).pack()
        entry = Entry(dynamic_frame, font=(font_family, 18))
        entry.pack()
        entries.append(entry)

        error_label = Label(dynamic_frame, text="", font=(font_family, 14), fg="red", bg=bg_color)
        error_label.pack()
        error_labels.append(error_label)

    name_entry, age_entry, id_entry, email_entry, phone_entry = entries
    name_error, age_error, id_error, email_error, phone_error = error_labels

    name_entry.bind("<Key>", lambda event: clear_error_label(event, name_error))
    age_entry.bind("<Key>", lambda event: clear_error_label(event, age_error))
    id_entry.bind("<Key>", lambda event: clear_error_label(event, id_error))
    email_entry.bind("<Key>", lambda event: clear_error_label(event, email_error))
    phone_entry.bind("<Key>", lambda event: clear_error_label(event, phone_error))

    Button(dynamic_frame, text="Add", font=(font_family, 18), bg=button_color, fg="white", command=perform_add).pack(pady=10)


def print_all():
    for widget in dynamic_frame.winfo_children():
        widget.destroy()

    Label(dynamic_frame, text="All Students", font=(font_family, 24), fg=font_color, bg=bg_color).pack(pady=10)
    scroll_text = st.ScrolledText(dynamic_frame, wrap=WORD, font=(font_family, 18), width=40, height=20, bg="white")
    scroll_text.pack(fill="both", expand=True)

    scroll_text.config(state=NORMAL)
    scroll_text.delete("1.0", END)
    for student in stu.allstudents:
        scroll_text.insert(END, f"{str(student)}\n")
    scroll_text.config(state=DISABLED)

def login():
    entered_id = login_entry.get()
    with open("studentlist.txt", "r") as f:
        students = f.readlines()
            
    ids = [line.strip().split(",")[2] for line in students if len(line.strip().split(",")) >= 3]
        
    if entered_id in ids:
        login_frame.pack_forget()
        main_menu.pack(side="left", fill="y")
        float_frame.pack(side="left", fill="both", expand=True)
        for line in students:
            details = line.strip().split(",")
            if len(details) >= 5 and details[2] == entered_id:
                stu.setFirstName(details[0])
                stu.setAge(details[1])
                stu.setIDNum(details[2])
                stu.setEmail(details[3])
                stu.setPhoneNumber(details[4])
        welcome_label.config(text=f"Welcome, {stu.getName()}!")
    else:
        error_label.config(text="ID not found! Please enter a valid ID.")



floatl_frame = Frame(login_frame, bg=frame_color, padx=20, pady=20, relief="solid")
floatl_frame.place(relx=0.5, rely=0.5, anchor="center")

Label(floatl_frame, text="Login to Continue", font=(font_family, 20), fg=font_color, bg=frame_color, padx=20).pack()
login_entry = Entry(floatl_frame, width=20, font=(font_family, 20))
login_entry.pack()
Button(floatl_frame, text="Login", width=20, font=(font_family, 20), bg=button_color, fg="white", command=login).pack()
error_label = Label(floatl_frame, text="", font=(font_family, 14), fg="red", bg=frame_color)
error_label.pack()

logout_button = Button(main_menu, text="Logout", width=20, font=(font_family, 20), bg=button_color, fg="white", padx=10, pady=15, command=logout)
logout_button.grid(row=5, column=0)
Label(main_menu, text="Main Menu", font=(font_family, 20), fg="white", bg=button_color, padx=20).grid(row=0, column=0)

btn_txt = ["View Your Information", "Search Student", "Add Student", "See All Students"]
btn_commands = [view_your, search_stud, add_stud, print_all]
buttons = []
for i, txt in enumerate(btn_txt):
    buttons.append(Button(main_menu, anchor="e", width=20, text=txt, font=(font_family, 20), bg=button_color, fg="white", padx=10, pady=15, command=btn_commands[i]))
    buttons[-1].grid(row=i+1, column=0)

welcome_label = Label(main_menu, text="Welcome!", font=(font_family, 20), fg="white", bg=button_color, padx=20)
welcome_label.grid(row=0, column=0)

win.mainloop()
