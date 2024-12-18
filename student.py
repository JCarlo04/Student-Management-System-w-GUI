class StudentInfo:

    def addStudent(self, name, age, idnum, email, phone):
            new_student = StudentInfo(name=name, age=age, idnum=idnum, email=email, phone=phone)
            self.allstudents.append(new_student)

    def __init__(self):
        self.allstudents = []

    def setFirstName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def setIDNum(self, idnum):
        self.idnum = idnum

    def setEmail(self, email):
        self.email = email

    def setPhoneNumber(self, phone):
        self.phone = phone

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def getIDNum(self):
        return self.idnum
    
    def getEmail(self):
        return self.email
    
    def getPhone(self):
        return self.phone
    
    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nID Number: {self.idnum}\nEmail: {self.email}\nPhone Number: {self.phone}"
    
    def read(self):
        self.allstudents = []
        with open("studentlist.txt", "r") as f:
            for line in f:
                line_strip = line.strip().split(",")
                if len(line_strip) == 5:
                    student = StudentInfo()
                    student.setFirstName(line_strip[0])
                    student.setAge(line_strip[1])
                    student.setIDNum(line_strip[2])
                    student.setEmail(line_strip[3])
                    student.setPhoneNumber(line_strip[4])
                    self.allstudents.append(student)
                else:
                    print(f"Skipping invalid line: {line.strip()}")
        


