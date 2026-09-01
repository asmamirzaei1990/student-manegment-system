class University:
    def __init__(self, university_id, name, city, address, phone, email, website, established_year, student_count, faculty_count, department):
        self.university_id = university_id
        self.name = name
        self.city = city
        self.address = address
        self.phone = phone
        self.email = email
        self.website = website
        self.established_year = established_year
        self.student_count = student_count
        self.faculty_count = faculty_count
        self.department = department

    def __repr__(self):
        return f"University({self.university_id!r}, {self.name!r})"
