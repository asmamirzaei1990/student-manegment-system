class University:
   
   def __init__(self,university_id,name,city,address,phone,email,website,established_year,student_count,faculty_count,department):
       
     self.university_id = university_id
     self.name = name
     self.city = city
     self.address = address  
     self.phone = phone  
     self.email  = email
     self.website  = website 
     self.established_year = established_year
     self.student_count = student_count
     self.faculty_count  = faculty_count
     self.department = department
     
   def show(self):
       print(f'id:{self.university_id}\n name:{self.name}\n city:{self.city}\naddress{self.address}\n phone:{self.phone}\nemaile:{self.email}\nwebsite:{self.website}\nestablished_year:\n{self.established_year}\nstudent_count:\n{self.student_count}\nfaculty_count:\n{self.faculty_count}\n department:{self.department}')

university1 = University(
    "U001",
    "University of Tehran",
    "Tehran",
    "Enghelab Street",
    "02161111",
    "info@ut.ac.ir",
    "https://ut.ac.ir",
    1934,
    50000,
    2000,
    "Computer Science"
)
university1.show()


class Professor:
      def __init__(self,teacher_id,first_name,last_name,age,phone,email,degree,specialization,department,employment_type):
        
        self.teacher_id = teacher_id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone = phone
        self.email = email
        self.degree = degree
        self.specialization = specialization
        self.department = department
        self.employment_type = employment_type
        self.courses = []
        

      def show (self):
        print(f'{self.teacher_id}\n first name{self.first_name} last name{self.last_name }age{self.age }Degree{self.degree }numer phone{self.phone}Email{self.email } specialization{self.specialization}department{self.department}courses{self.courses}')
      

professor1 = Professor( 'T001', 'Ali', 'Ahmadi', 45, 12345678, 'Ali.ahmadi@gmail.com', 'PhD', 'Artificial Intelligence', 'Computer Science', 'Full-time')
professor2 = Professor( 'T002', 'Sara', 'Mohammadi', 38, 12345678, 'Sara.Mohamadi@gmail.com', 'PhD', 'Software Engineering', 'Computer Science', 'Full-time')

professor3 = Professor('T003','Reza','Karimi',51,12345678,'Reza.Karimi@gmail.com','PhD','Computer Networks','Computer Engineering','Full-time')
professor4 = Professor('T004','Maryam','Hosseini',34,12345678,'Reza.Hosseini@gmail.com','MSc','Database Systems','Computer Science','Part-time')

professor5 = Professor('T005','Arman','Rahimi',42,12345678,'Armaan.Rahimi@gmail.com','PhD','Machine Learning','Computer Science','Full-time')
professor6 = Professor('T006','Neda','Moradi',37,12345678,'Neda.Moradi@gmail.com','PhD','Human-Computer-Interaction','Computer Engineering','Full-time')

professor7 = Professor( 'T007','Hassan','Ebrahimi', 49, 12345678,'Hasan.Moradi@gmail.com','PhD','Operating Systems','Computer Engineering','Full-time')
professor8 = Professor('T008','Leila','Ahmadi',32,12345678,'Laila.Ahmadi@gmail.com','MSc','Web Development','Computer Science','Part-time')

professor9 = Professor('T009','Kamran','Safari',55,12345678,'Kamran.Safari@gmail.com','PhD','Computer Architecture','Computer Engineering','Full-time')
professor10 = Professor('T010','Shirin','Ghasemi',40,12345678,'Shirin.Gasemi@gmail.com','PhD','Data Science','Computer Science','Full-time')

professor1.show()    
professor2.show()    
professor3.show()    
professor4.show()    
professor5.show()    
professor6.show()    
professor7.show()    
professor8.show()    
professor9.show()    
professor10.show()   





class Student:

    def __init__(
        self,
        student_id,
        first_name,
        last_name,
        age,
        birth_place,
        major,
        semester,
        email,
        phone,
        gpa
    ):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.birth_place = birth_place
        self.major = major
        self.semester = semester
        self.email = email
        self.phone = phone
        self.gpa = gpa
        self.enrollments = []




students_data = [
    ('S001', 'Amir', 'Hosseini', 21, 'Tehran', 'Computer Science', 4, 'amir.hosseini@gmail.com', '9123456701', 17.8),
    ('S002', 'Sara', 'Ahmadi', 22, 'Shiraz', 'Software Engineering', 6, 'sara.ahmadi@gmail.com', '9123456702', 18.5),
    ('S003', 'Reza', 'Karimi', 20, 'Tabriz', 'Computer Engineering', 3, 'reza.karimi@gmail.com', '9123456703', 16.9),
    ('S004', 'Neda', 'Moradi', 23, 'Isfahan', 'Computer Science', 8, 'neda.moradi@gmail.com', '9123456704', 19.1),

    ('S005', 'Ali', 'Mohammadi', 21, 'Mashhad', 'Software Engineering', 4, 'ali.mohammadi@gmail.com', '9123456705', 15.7),
    ('S006', 'Maryam', 'Rahimi', 22, 'Rasht', 'Computer Engineering', 6, 'maryam.rahimi@gmail.com', '9123456706', 18.2),
    ('S007', 'Hassan', 'Ebrahimi', 24, 'Kerman', 'Computer Science', 8, 'hassan.ebrahimi@gmail.com', '9123456707', 16.4),
    ('S008', 'Leila', 'Ahmadi', 20, 'Sanandaj', 'Software Engineering', 2, 'leila.ahmadi@gmail.com', '9123456708', 19.3),

    ('S009', 'Arman', 'Rahimi', 23, 'Qom', 'Computer Engineering', 6, 'arman.rahimi@gmail.com', '9123456709', 17.1),
    ('S010', 'Shirin', 'Ghasemi', 21, 'Yazd', 'Computer Science', 4, 'shirin.ghasemi@gmail.com', '9123456710', 18.7),
    ('S011', 'Mehdi', 'Jafari', 22, 'Tehran', 'Software Engineering', 6, 'mehdi.jafari@gmail.com', '9123456711', 16.8),
    ('S012', 'Fatemeh', 'Sadeghi', 20, 'Shiraz', 'Computer Science', 3, 'fatemeh.sadeghi@gmail.com', '9123456712', 17.5),

    ('S013', 'Pouya', 'Niknam', 24, 'Mashhad', 'Computer Engineering', 8, 'pouya.niknam@gmail.com', '9123456713', 15.9),
    ('S014', 'Zahra', 'Kazemi', 21, 'Isfahan', 'Software Engineering', 4, 'zahra.kazemi@gmail.com', '9123456714', 18.9),
    ('S015', 'Sina', 'Hashemi', 23, 'Tabriz', 'Computer Science', 6, 'sina.hashemi@gmail.com', '9123456715', 17.3),
    ('S016', 'Mina', 'Rostami', 20, 'Kermanshah', 'Computer Engineering', 2, 'mina.rostami@gmail.com', '9123456716', 19.0),

    ('S017', 'Omid', 'Nouri', 22, 'Ahvaz', 'Computer Science', 4, 'omid.nouri@gmail.com', '9123456717', 16.2),
    ('S018', 'Elahe', 'Mousavi', 23, 'Tehran', 'Software Engineering', 8, 'elahe.mousavi@gmail.com', '9123456718', 18.1),
    ('S019', 'Kian', 'Shahriari', 21, 'Rasht', 'Computer Engineering', 4, 'kian.shahriari@gmail.com', '9123456719', 17.6),
    ('S020', 'Nazanin', 'Etemadi', 22, 'Qazvin', 'Computer Science', 6, 'nazanin.etemadi@gmail.com', '9123456720', 19.2),

    ('S021', 'Mohammad', 'Yousefi', 24, 'Mashhad', 'Software Engineering', 8, 'mohammad.yousefi@gmail.com', '9123456721', 15.8),
    ('S022', 'Parisa', 'Shahbazi', 20, 'Tehran', 'Computer Science', 2, 'parisa.shahbazi@gmail.com', '9123456722', 18.6),
    ('S023', 'Amin', 'Fattahi', 21, 'Sanandaj', 'Computer Engineering', 4, 'amin.fattahi@gmail.com', '9123456723', 17.0),
    ('S024', 'Hanieh', 'Mansouri', 23, 'Shiraz', 'Software Engineering', 6, 'hanieh.mansouri@gmail.com', '9123456724', 18.4),

    ('S025', 'Kasra', 'Rahmani', 22, 'Isfahan', 'Computer Science', 6, 'kasra.rahmani@gmail.com', '9123456725', 16.7),
    ('S026', 'Yasmin', 'Akbari', 21, 'Tabriz', 'Computer Engineering', 4, 'yasmin.akbari@gmail.com', '9123456726', 19.4),
    ('S027', 'Saeed', 'Mokhtari', 24, 'Kerman', 'Computer Science', 8, 'saeed.mokhtari@gmail.com', '9123456727', 15.5),
    ('S028', 'Roya', 'Vahidi', 20, 'Tehran', 'Software Engineering', 2, 'roya.vahidi@gmail.com', '9123456728', 18.8),

    ('S029', 'Farhad', 'Samadi', 23, 'Yazd', 'Computer Engineering', 6, 'farhad.samadi@gmail.com', '9123456729', 17.9),
    ('S030', 'Sahar', 'Zarei', 22, 'Rasht', 'Computer Science', 4, 'sahar.zarei@gmail.com', '9123456730', 16.5),
    ('S031', 'Navid', 'Khosravi', 21, 'Mashhad', 'Software Engineering', 4, 'navid.khosravi@gmail.com', '9123456731', 18.0),
    ('S032', 'Arezoo', 'Eslami', 23, 'Tehran', 'Computer Science', 8, 'arezoo.eslami@gmail.com', '9123456732', 17.2),

    ('S033', 'Milad', 'Abbasi', 20, 'Qom', 'Computer Engineering', 2, 'milad.abbasi@gmail.com', '9123456733', 16.9),
    ('S034', 'Tara', 'Jalali', 22, 'Shiraz', 'Software Engineering', 6, 'tara.jalali@gmail.com', '9123456734', 19.0),
    ('S035', 'Behzad', 'Shafiei', 24, 'Isfahan', 'Computer Science', 8, 'behzad.shafiei@gmail.com', '9123456735', 15.3),
    ('S036', 'Mona', 'Karimi', 21, 'Kermanshah', 'Computer Engineering', 4, 'mona.karimi@gmail.com', '9123456736', 18.3),

    ('S037', 'Shayan', 'Taheri', 22, 'Tehran', 'Computer Science', 6, 'shayan.taheri@gmail.com', '9123456737', 17.7),
    ('S038', 'Ayla', 'Moradi', 20, 'Sanandaj', 'Software Engineering', 2, 'ayla.moradi@gmail.com', '9123456738', 19.5),
    ('S039', 'Ramin', 'Shirazi', 23, 'Shiraz', 'Computer Engineering', 6, 'ramin.shirazi@gmail.com', '9123456739', 16.1),
    ('S040', 'Mahsa', 'Naderi', 21, 'Yazd', 'Computer Science', 4, 'mahsa.naderi@gmail.com', '9123456740', 18.7),

    ('S041', 'Daniyal', 'Gholami', 24, 'Ahvaz', 'Software Engineering', 8, 'daniyal.gholami@gmail.com', '9123456741', 17.4),
    ('S042', 'Samira', 'Bahrami', 22, 'Rasht', 'Computer Science', 6, 'samira.bahrami@gmail.com', '9123456742', 18.9),
    ('S043', 'Ehsan', 'Kiani', 20, 'Tabriz', 'Computer Engineering', 2, 'ehsan.kiani@gmail.com', '9123456743', 16.8),
    ('S044', 'Negar', 'Soleimani', 23, 'Tehran', 'Software Engineering', 8, 'negar.soleimani@gmail.com', '9123456744', 19.1),

    ('S045', 'Morteza', 'Azizi', 21, 'Kerman', 'Computer Science', 4, 'morteza.azizi@gmail.com', '9123456745', 15.9),
    ('S046', 'Hoda', 'Nasiri', 22, 'Isfahan', 'Computer Engineering', 6, 'hoda.nasiri@gmail.com', '9123456746', 18.0),
    ('S047', 'Soroush', 'Maleki', 24, 'Mashhad', 'Software Engineering', 8, 'soroush.maleki@gmail.com', '9123456747', 17.6),

    ('S048', 'Atena', 'Ranjbar', 20, 'Sanandaj', 'Computer Science', 2, 'atena.ranjbar@gmail.com', '9123456748', 19.3),
    ('S049', 'Yasin', 'Rahimi', 23, 'Qazvin', 'Computer Engineering', 6, 'yasin.rahimi@gmail.com','9123456749', 16.6),
    ('S050', 'Kimia', 'Pourmohammadi', 21, 'Tehran', 'Software Engineering', 4, 'kimia.pourmohammadi@gmail.com', '9123456750', 18.5)
]      

students = []
for data in students_data:
    student = Student(*data)
    students.append(student)



def add_student():
    student_id = input("Enter student ID: ")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    age = int(input("Enter age: "))
    birth_place = input("Enter birth place: ")
    major = input("Enter major: ")
    semester = int(input("Enter semester: "))
    email = input("Enter email: ")
    phone = input("Enter phone: ")
    gpa = float(input("Enter GPA: "))

    student = Student(
        student_id,
        first_name,
        last_name,
        age,
        birth_place,
        major,
        semester,
        email,
        phone,
        gpa
    )
    students.append(student)
    print("Student added successfully!")



 
def get_students():
    if not students:
        print("No students found!")
        return
    for student in students:
        print(
            student.student_id,
            student.first_name,
            student.last_name,
            student.major,
            student.gpa
        )



def get_student():
    student_id = input("Enter student ID: ")
    for student in students:
        if student.student_id == student_id:
            print("Student found!")
            print("ID:", student.student_id)
            print("Name:", student.first_name, student.last_name)
            print("Age:", student.age)
            print("Birth place:", student.birth_place)
            print("Major:", student.major)
            print("Semester:", student.semester)
            print("Email:", student.email)
            print("Phone:", student.phone)
            print("GPA:", student.gpa)
            return
    print("Student not found!")



 
def search_student():
    keyword = input("Enter name to search: ").lower()
    found = False
    for student in students:
        full_name = student.first_name + " " + student.last_name
        if keyword in full_name.lower():
            print(
                student.student_id,
                student.first_name,
                student.last_name,
                student.major,
                student.gpa
            )
            found = True
    if not found:
        print("No student found!")


 
def update_student():
    student_id = input("Enter student ID: ")
    for student in students:
        if student.student_id == student_id:
            student.first_name = input("Enter new first name: ")
            student.last_name = input("Enter new last name: ")
            student.age = int(input("Enter new age: "))
            student.birth_place = input("Enter new birth place: ")
            student.major = input("Enter new major: ")
            student.semester = int(input("Enter new semester: "))
            student.email = input("Enter new email: ")
            student.phone = input("Enter new phone: ")
            student.gpa = float(input("Enter new GPA: "))
            print("Student updated successfully!")
            return
    print("Student not found!")



def delete_student():
    student_id = input("Enter student ID: ")
    for student in students:
        if student.student_id == student_id:
            students.remove(student)
            print("Student deleted successfully!")
            return
    print("Student not found!")


def is_student(birth_place):
    if birth_place.lower() == "tehran":
        print("No accept at dormitory")
    else:
        print("Accept at dormitory")



while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Show Student")
    print("4. Search Student")
    print("5. Update Student")
    print("6. Delete Student")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        get_students()

    elif choice == "3":
        get_student()

    elif choice == "4":
        search_student()

    elif choice == "5":
        update_student()

    elif choice == "6":
        delete_student()

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")



       
class Course:
     def __init__(self, course_id, name, units, teacher,capacity, semester, department,day, start_time, end_time, room):

        self.course_id = course_id
        self.name = name
        self.units = units
        self.teacher = teacher
        self.capacity = capacity
        self.semester = semester
        self.department = department
        self.day = day
        self.start_time = start_time
        self.end_time = end_time
        self.room = room
        self.students = []
        self.enrollments = []

courses_data = [
    ('CS101', 'Introduction to Programming', 3, professor10, 45, 6,'Computer Science', 'Monday', '14:00', '16:00', 'Room 102'),
    ('CS102', 'Object-Oriented Programming', 3, professor6, 21, 7, 'Computer Science', 'Tuesday', '08:00', '12:00', 'Room 108'),

    ('CS103', 'Data Structures', 3, professor3, 38, 4,'Computer Science', 'Friday', '10:00', '12:00', 'Room 103'),
    ('CS104', 'Algorithms', 3, professor5, 52, 6,'Computer Science', 'Wednesday', '08:00', '10:00', 'Room 106'),

    ('CS105', 'Discrete Mathematics', 3, professor7, 27, 4, 'Computer Science', 'Tuesday', '14:00', '16:00', 'Room 107'),
    ('CS106', 'Database Systems', 3, professor6, 29, 7,'Computer Science', 'Wednesday', '16:00', '20:00', 'Room 109'),

    ('CS107', 'Computer Architecture', 3, professor5, 31, 2, 'Computer Science', 'Monday', '08:00', '10:00', 'Room 102'),
    ('CS108', 'Operating Systems', 3, professor10, 45, 3,'Computer Science', 'Tuesday', '10:00', '12:00', 'Room 105'),
    
    ('CS109', 'Computer Networks', 3, professor5, 40, 3,'Computer Science', 'Wednesday', '08:00', '10:00', 'Room 109'),
    ('CS110', 'Software Engineering', 3, professor3, 34, 7,'Computer Science', 'Thursday', '14:00', '16:00', 'Room 104'),

    ('CS111', 'Artificial Intelligence', 3, professor10, 25, 8,'Computer Science', 'Monday', '16:00', '18:00', 'Room 110'),
    ('CS112', 'Machine Learning', 3, professor5, 30, 8, 'Computer Science', 'Thursday', '10:00', '12:00', 'Room 111')
]

courses = []

for data in courses_data:
    course = Course(*data)
    courses.append(course)

for course in courses:
    course.teacher.courses.append(course)

for course in courses:
    print(course.course_id)
    print(course.name)
    print(course.teacher.first_name)
    print(course.capacity)
    print(course.day)
    print(course.start_time)
    print(course.end_time)
    print(course.room)

for course in professor10.courses:
    print(course.name)



class Enrollment:
    def __init__(self, enrollment_id, student, course,enrollment_date, 
                 status, grade):

        self.enrollment_id = enrollment_id
        self.student = student
        self.course = course
        self.enrollment_date = enrollment_date
        self.status = status
        self.grade = grade


enrollments_data = [

    ('E001', students[0], courses[0], '2026-08-01', 'Active', None),
    ('E002', students[1], courses[0], '2026-08-01', 'Active', None),
    ('E003', students[2], courses[1], '2026-08-02', 'Active', None),
    ('E004', students[3], courses[2], '2026-08-02', 'Active', None),
    ('E005', students[4], courses[3], '2026-08-03', 'Active', None),

    ('E006', students[5], courses[4], '2026-08-03', 'Active', None),
    ('E007', students[6], courses[5], '2026-08-04', 'Active', None),
    ('E008', students[7], courses[6], '2026-08-04', 'Active', None),
    ('E009', students[8], courses[7], '2026-08-05', 'Active', None),
    ('E010', students[9], courses[8], '2026-08-05', 'Active', None),

    ('E011', students[10], courses[9], '2026-08-06', 'Active', None),
    ('E012', students[11], courses[10], '2026-08-06', 'Active', None),
    ('E013', students[12], courses[11], '2026-08-07', 'Active', None),
    ('E014', students[13], courses[0], '2026-08-07', 'Active', None),
    ('E015', students[14], courses[1], '2026-08-08', 'Active', None),

    ('E016', students[15], courses[2], '2026-08-08', 'Active', None),
    ('E017', students[16], courses[3], '2026-08-09', 'Active', None),
    ('E018', students[17], courses[4], '2026-08-09', 'Active', None),
    ('E019', students[18], courses[5], '2026-08-10', 'Active', None),
    ('E020', students[19], courses[6], '2026-08-10', 'Active', None),

    ('E021', students[20], courses[7], '2026-08-11', 'Active', None),
    ('E022', students[21], courses[8], '2026-08-11', 'Active', None),
    ('E023', students[22], courses[9], '2026-08-12', 'Active', None),
    ('E024', students[23], courses[10], '2026-08-12', 'Active', None),
    ('E025', students[24], courses[11], '2026-08-13', 'Active', None),

    ('E026', students[25], courses[0], '2026-08-13', 'Active', None),
    ('E027', students[26], courses[1], '2026-08-14', 'Active', None),
    ('E028', students[27], courses[2], '2026-08-14', 'Active', None),
    ('E029', students[28], courses[3], '2026-08-15', 'Active', None),
    ('E030', students[29], courses[4], '2026-08-15', 'Active', None),

    ('E031', students[30], courses[5], '2026-08-16', 'Active', None),
    ('E032', students[31], courses[6], '2026-08-16', 'Active', None),
    ('E033', students[32], courses[7], '2026-08-17', 'Active', None),
    ('E034', students[33], courses[8], '2026-08-17', 'Active', None),
    ('E035', students[34], courses[9], '2026-08-18', 'Active', None),

    ('E036', students[35], courses[10], '2026-08-18', 'Active', None),
    ('E037', students[36], courses[11], '2026-08-18', 'Active', None),
    ('E038', students[37], courses[0], '2026-08-18', 'Active', None),
    ('E039', students[38], courses[1], '2026-08-18', 'Active', None),
    ('E040', students[39], courses[2], '2026-08-18', 'Active', None),

    ('E041', students[40], courses[3], '2026-08-18', 'Active', None),
    ('E042', students[41], courses[4], '2026-08-18', 'Active', None),
    ('E043', students[42], courses[5], '2026-08-18', 'Active', None),
    ('E044', students[43], courses[6], '2026-08-18', 'Active', None),
    ('E045', students[44], courses[7], '2026-08-18', 'Active', None),

    ('E046', students[45], courses[8], '2026-08-18', 'Active', None),
    ('E047', students[46], courses[9], '2026-08-18', 'Active', None),
    ('E048', students[47], courses[10], '2026-08-18', 'Active', None),
    ('E049', students[48], courses[11], '2026-08-18', 'Active', None),
    ('E050', students[49], courses[0], '2026-08-18', 'Active', None)
]

enrollments = []

for data in enrollments_data:
    enrollment = Enrollment(*data)
    enrollments.append(enrollment)

print(enrollments[0].enrollment_id)
print(enrollments[0].student.first_name)
print(enrollments[0].student.last_name)
print(enrollments[0].course.name)
print(enrollments[0].enrollment_date)
print(enrollments[0].status)
print(enrollments[0].grade)     

for enrollment in enrollments:
    enrollment.student.enrollments.append(enrollment)

for enrollment in enrollments:
    enrollment.course.enrollments.append(enrollment)



class Grade:
    def __init__(self, grade_id, student, course, score, date):
        self.grade_id = grade_id
        self.student = student
        self.course = course
        self.score = score
        self.date = date


grade_data = [

    ('G001', students[0], courses[0], 17.5, '2026-08-10'),
    ('G002', students[1], courses[0], 18.0, '2026-08-10'),
    ('G003', students[2], courses[1], 16.5, '2026-08-11'),
    ('G004', students[3], courses[2], 19.0, '2026-08-11'),
    ('G005', students[4], courses[3], 15.5, '2026-08-12'),

    ('G006', students[5], courses[4], 18.5, '2026-08-12'),
    ('G007', students[6], courses[5], 16.0, '2026-08-13'),
    ('G008', students[7], courses[6], 19.5, '2026-08-13'),
    ('G009', students[8], courses[7], 17.0, '2026-08-14'),
    ('G010', students[9], courses[8], 18.5, '2026-08-14'),

    ('G011', students[10], courses[9], 16.5, '2026-08-15'),
    ('G012', students[11], courses[10], 19.0, '2026-08-15'),
    ('G013', students[12], courses[11], 15.0, '2026-08-16'),
    ('G014', students[13], courses[0], 18.0, '2026-08-16'),
    ('G015', students[14], courses[1], 17.5, '2026-08-17'),

    ('G016', students[15], courses[2], 19.0, '2026-08-17'),
    ('G017', students[16], courses[3], 16.0, '2026-08-18'),
    ('G018', students[17], courses[4], 18.5, '2026-08-18'),
    ('G019', students[18], courses[5], 17.0, '2026-08-18'),
    ('G020', students[19], courses[6], 19.5, '2026-08-18'),

    ('G021', students[20], courses[7], 15.5, '2026-08-18'),
    ('G022', students[21], courses[8], 18.0, '2026-08-18'),
    ('G023', students[22], courses[9], 16.5, '2026-08-18'),
    ('G024', students[23], courses[10], 19.0, '2026-08-18'),
    ('G025', students[24], courses[11], 17.5, '2026-08-18'),

    ('G026', students[25], courses[0], 18.5, '2026-08-18'),
    ('G027', students[26], courses[1], 16.0, '2026-08-18'),
    ('G028', students[27], courses[2], 19.5, '2026-08-18'),
    ('G029', students[28], courses[3], 17.0, '2026-08-18'),
    ('G030', students[29], courses[4], 15.5, '2026-08-18'),

    ('G031', students[30], courses[5], 18.0, '2026-08-18'),
    ('G032', students[31], courses[6], 17.5, '2026-08-18'),
    ('G033', students[32], courses[7], 16.5, '2026-08-18'),
    ('G034', students[33], courses[8], 19.0, '2026-08-18'),
    ('G035', students[34], courses[9], 15.0, '2026-08-18'),

    ('G036', students[35], courses[10], 18.5, '2026-08-18'),
    ('G037', students[36], courses[11], 17.0, '2026-08-18'),
    ('G038', students[37], courses[0], 19.5, '2026-08-18'),
    ('G039', students[38], courses[1], 16.0, '2026-08-18'),
    ('G040', students[39], courses[2], 18.0, '2026-08-18'),

    ('G041', students[40], courses[3], 17.5, '2026-08-18'),
    ('G042', students[41], courses[4], 19.0, '2026-08-18'),
    ('G043', students[42], courses[5], 16.5, '2026-08-18'),
    ('G044', students[43], courses[6], 18.5, '2026-08-18'),
    ('G045', students[44], courses[7], 15.5, '2026-08-18'),

    ('G046', students[45], courses[8], 17.0, '2026-08-18'),
    ('G047', students[46], courses[9], 19.0, '2026-08-18'),
    ('G048', students[47], courses[10], 18.5, '2026-08-18'),
    ('G049', students[48], courses[11], 16.0, '2026-08-18'),
    ('G050', students[49], courses[0], 18.0, '2026-08-18')
]


grades = []

for data in grade_data:
    grade = Grade(*data)
    grades.append(grade)

print(grades[0].grade_id)
print(grades[0].student.first_name)
print(grades[0].student.last_name)
print(grades[0].course.name)
print(grades[0].score)
print(grades[0].date)
 