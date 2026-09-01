import os
from database import Database
from repositories.student_repository import StudentRepository
from repositories.professor_repository import ProfessorRepository
from repositories.course_repository import CourseRepository
from repositories.enrollment_repository import EnrollmentRepository
from repositories.grade_repository import GradeRepository
from services import StudentService, EnrollmentService, GradeService
from exceptions import DuplicateError, CapacityError, ValidationError


def setup_db(tmp_path):
    db=Database(tmp_path/"test.db");db.initialize();db.seed_if_empty();return db

def test_student_crud(tmp_path):
    db=setup_db(tmp_path);s=StudentService(StudentRepository(db))
    sid="TEST001"
    s.add(dict(student_id=sid,first_name="Test",last_name="User",age="22",birth_place="Tehran",major="CS",semester="2",email="test@example.com",phone="09120000000",gpa="18.5"))
    assert s.get(sid).full_name=="Test User"
    s.update(sid,{"first_name":"Updated","last_name":"User","age":"23","birth_place":"Shiraz","major":"CS","semester":"3","email":"test@example.com","phone":"09120000000","gpa":"19"})
    assert s.get(sid).first_name=="Updated"
    s.delete(sid)
    assert s.repo.get_by_id(sid) is None

def test_duplicate_enrollment_is_rejected(tmp_path):
    db=setup_db(tmp_path);er=EnrollmentService(EnrollmentRepository(db),StudentRepository(db),CourseRepository(db))
    try: er.add({"enrollment_id":"E999","student_id":"S001","course_id":"CS101","enrollment_date":"2026-08-31","status":"Active"})
    except DuplicateError: return
    assert False

def test_grade_requires_enrollment(tmp_path):
    db=setup_db(tmp_path);gr=GradeService(GradeRepository(db),StudentRepository(db),CourseRepository(db),EnrollmentRepository(db))
    try: gr.add({"grade_id":"G999","student_id":"S001","course_id":"CS112","score":"18","date":"2026-08-31"})
    except ValidationError: return
    assert False
