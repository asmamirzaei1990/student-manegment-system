class Course:
    def __init__(self, course_id, name, units, teacher, capacity, semester, department, day, start_time, end_time, room):
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

    def __repr__(self):
        return f"Course({self.course_id!r}, {self.name!r})"
