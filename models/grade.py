class Grade:
    def __init__(self, grade_id, student, course, score, date):
        self.grade_id = grade_id
        self.student = student
        self.course = course
        self.score = score
        self.date = date

    def __repr__(self):
        return f"Grade({self.grade_id!r}, {self.score})"
