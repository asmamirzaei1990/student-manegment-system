class Professor:
    def __init__(self, professor_id, first_name, last_name, age, phone, email, degree, specialization, department, employment_type):
        self.professor_id = professor_id
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

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"Professor({self.professor_id!r}, {self.full_name!r})"
