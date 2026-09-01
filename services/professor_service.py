import logging, sqlite3
from models import Professor
from exceptions import DuplicateError, NotFoundError
from validators import required, positive_int, email
class ProfessorService:
    def __init__(self,repo):self.repo=repo
    def get_all(self):return self.repo.get_all()
    def get(self,pid):
        p=self.repo.get_by_id(pid)
        if not p:raise NotFoundError("Professor not found.")
        return p
    def search(self,k):return self.repo.search_by_name(k)
    def add(self,data):
        required(data["professor_id"],"Professor ID")
        if self.repo.get_by_id(data["professor_id"]):raise DuplicateError("Professor ID already exists.")
        data=dict(data);data["age"]=positive_int(data["age"],"Age");email(data.get("email",""));self.repo.add(Professor(**data));logging.info("Professor added: %s",data["professor_id"])
    def update(self,pid,data):
        self.get(pid);data=dict(data);data["age"]=positive_int(data["age"],"Age");email(data.get("email",""));self.repo.update(pid,data);logging.info("Professor updated: %s",pid)
    def delete(self,pid):
        self.get(pid)
        try:self.repo.delete(pid)
        except sqlite3.IntegrityError: raise NotFoundError("Professor cannot be deleted while assigned to a course.")
        logging.info("Professor deleted: %s",pid)
