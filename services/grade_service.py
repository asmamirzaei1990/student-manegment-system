import logging, sqlite3
from models import Grade
from exceptions import DuplicateError, NotFoundError, ValidationError
from validators import range_float
class GradeService:
    def __init__(self,repo,student_repo,course_repo,enrollment_repo):self.repo=repo;self.student_repo=student_repo;self.course_repo=course_repo;self.enrollment_repo=enrollment_repo
    def get_all(self):return self.repo.get_all()
    def get(self,gid):
        g=self.repo.get_by_id(gid)
        if not g:raise NotFoundError("Grade not found.")
        return g
    def search(self,k):return self.repo.find_by_student_or_course(k)
    def _validate_pair(self,sid,cid):
        if not self.student_repo.get_by_id(sid):raise NotFoundError("Student not found.")
        if not self.course_repo.get_by_id(cid):raise NotFoundError("Course not found.")
        if not self.enrollment_repo.exists_student_course(sid,cid):raise ValidationError("A grade requires an enrollment for this student and course.")
    def add(self,data):
        if self.repo.get_by_id(data["grade_id"]):raise DuplicateError("Grade ID already exists.")
        self._validate_pair(data["student_id"],data["course_id"]);score=range_float(data["score"],0,20,"Score")
        try:self.repo.add(Grade(data["grade_id"],data["student_id"],data["course_id"],score,data["date"]))
        except sqlite3.IntegrityError:raise DuplicateError("A grade already exists for this student and course.")
        logging.info("Grade added: %s",data["grade_id"])
    def update(self,gid,data):
        self.get(gid);self._validate_pair(data["student_id"],data["course_id"]);data=dict(data);data["score"]=range_float(data["score"],0,20,"Score")
        try:self.repo.update(gid,data)
        except sqlite3.IntegrityError:raise DuplicateError("A grade already exists for this student and course.")
    def delete(self,gid):self.get(gid);self.repo.delete(gid);logging.info("Grade deleted: %s",gid)
