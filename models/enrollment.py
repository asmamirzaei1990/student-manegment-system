class Enrollment:
    def __init__(self, enrollment_id, student, course, enrollment_date, status="Active", grade=None):
        self.enrollment_id = enrollment_id
        self.student = student
        self.course = course
        self.enrollment_date = enrollment_date
        self.status = status
        self.grade = grade

    def __repr__(self):
        return f"Enrollment({self.enrollment_id!r}, {self.student.student_id!r}, {self.course.course_id!r})"
