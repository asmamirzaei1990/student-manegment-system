import logging
from models import Student
from exceptions import DuplicateError, NotFoundError, ValidationError
from validators import required, positive_int, range_float, email

class StudentService:
    def __init__(self, repo): self.repo=repo
    def get_all(self): return self.repo.get_all()
    def get(self,sid):
        s=self.repo.get_by_id(sid)
        if not s: raise NotFoundError("Student not found.")
        return s
    def search(self,k): return self.repo.search_by_name(k)
    def add(self, data):
        required(data["student_id"],"Student ID")
        if self.repo.get_by_id(data["student_id"]): raise DuplicateError("Student ID already exists.")
        data=dict(data); data["age"]=positive_int(data["age"],"Age"); data["semester"]=positive_int(data["semester"],"Semester"); data["gpa"]=range_float(data["gpa"],0,20,"GPA"); email(data.get("email",""))
        self.repo.add(Student(**data)); logging.info("Student added: %s",data["student_id"])
    def update(self,sid,data):
        self.get(sid); data=dict(data); data["age"]=positive_int(data["age"],"Age"); data["semester"]=positive_int(data["semester"],"Semester"); data["gpa"]=range_float(data["gpa"],0,20,"GPA"); email(data.get("email",""))
        self.repo.update(sid,data); logging.info("Student updated: %s",sid)
    def delete(self,sid):
        self.get(sid); self.repo.delete(sid); logging.info("Student deleted: %s",sid)
