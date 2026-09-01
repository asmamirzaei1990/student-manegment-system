class Student:
    def __init__(self, student_id, first_name, last_name, age, birth_place, major, semester, email, phone, gpa):
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

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"Student({self.student_id!r}, {self.full_name!r})"
