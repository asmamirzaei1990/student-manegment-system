import logging, sqlite3
from models import Enrollment
from exceptions import DuplicateError, NotFoundError, CapacityError, ValidationError
class EnrollmentService:
    def __init__(self,repo,student_repo,course_repo):self.repo=repo;self.student_repo=student_repo;self.course_repo=course_repo
    def get_all(self):return self.repo.get_all()
    def get(self,eid):
        e=self.repo.get_by_id(eid)
        if not e:raise NotFoundError("Enrollment not found.")
        return e
    def search(self,k):return self.repo.find_by_student_or_course(k)
    def add(self,data):
        if self.repo.get_by_id(data["enrollment_id"]):raise DuplicateError("Enrollment ID already exists.")
        if not self.student_repo.get_by_id(data["student_id"]):raise NotFoundError("Student not found.")
        if not self.course_repo.get_by_id(data["course_id"]):raise NotFoundError("Course not found.")
        if self.repo.exists_student_course(data["student_id"],data["course_id"]):raise DuplicateError("Student is already enrolled in this course.")
        if self.course_repo.count_enrollments(data["course_id"])>=self.course_repo.get_by_id(data["course_id"]).capacity:raise CapacityError("Course capacity is full.")
        try:self.repo.add(Enrollment(data["enrollment_id"],data["student_id"],data["course_id"],data["enrollment_date"],data.get("status","Active")))
        except sqlite3.IntegrityError as e:raise ValidationError(str(e))
        logging.info("Enrollment added: %s",data["enrollment_id"])
    def update(self,eid,data):
        old=self.get(eid)
        if not self.student_repo.get_by_id(data["student_id"]):raise NotFoundError("Student not found.")
        if not self.course_repo.get_by_id(data["course_id"]):raise NotFoundError("Course not found.")
        if (data["student_id"],data["course_id"])!=(old.student,old.course) and self.repo.exists_student_course(data["student_id"],data["course_id"]):raise DuplicateError("Student is already enrolled in this course.")
        if data["course_id"]!=old.course and self.course_repo.count_enrollments(data["course_id"])>=self.course_repo.get_by_id(data["course_id"]).capacity:raise CapacityError("Course capacity is full.")
        try:self.repo.update(eid,data)
        except sqlite3.IntegrityError as e:raise ValidationError(str(e))
    def delete(self,eid):self.get(eid);self.repo.delete(eid);logging.info("Enrollment deleted: %s",eid)
