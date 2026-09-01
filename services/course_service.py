import logging, sqlite3
from models import Course
from exceptions import DuplicateError, NotFoundError, CapacityError, ValidationError
from validators import required, positive_int
class CourseService:
    def __init__(self,repo,professor_repo):self.repo=repo;self.professor_repo=professor_repo
    def get_all(self):return self.repo.get_all()
    def get(self,cid):
        c=self.repo.get_by_id(cid)
        if not c:raise NotFoundError("Course not found.")
        return c
    def search(self,k):return self.repo.search_by_name(k)
    def add(self,data):
        required(data["course_id"],"Course ID")
        if self.repo.get_by_id(data["course_id"]):raise DuplicateError("Course ID already exists.")
        if not self.professor_repo.get_by_id(data["teacher_id"]):raise NotFoundError("Professor not found.")
        data=dict(data);data["units"]=positive_int(data["units"],"Units");data["capacity"]=positive_int(data["capacity"],"Capacity");data["semester"]=positive_int(data["semester"],"Semester")
        self.repo.add(Course(**data));logging.info("Course added: %s",data["course_id"])
    def update(self,cid,data):
        self.get(cid)
        if not self.professor_repo.get_by_id(data["teacher_id"]):raise NotFoundError("Professor not found.")
        data=dict(data);data["units"]=positive_int(data["units"],"Units");data["capacity"]=positive_int(data["capacity"],"Capacity");data["semester"]=positive_int(data["semester"],"Semester")
        if data["capacity"] < self.repo.count_enrollments(cid):raise ValidationError("Capacity cannot be below current enrollment count.")
        self.repo.update(cid,data);logging.info("Course updated: %s",cid)
    def delete(self,cid):
        self.get(cid)
        if self.repo.count_enrollments(cid)>0:raise ValidationError("Cannot delete a course with enrolled students.")
        try:self.repo.delete(cid)
        except sqlite3.IntegrityError:raise ValidationError("Course cannot be deleted.")
        logging.info("Course deleted: %s",cid)
