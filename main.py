from database import Database
from repositories.student_repository import StudentRepository
from repositories.professor_repository import ProfessorRepository
from repositories.course_repository import CourseRepository
from repositories.enrollment_repository import EnrollmentRepository
from repositories.grade_repository import GradeRepository
from repositories.university_repository import UniversityRepository
from services import StudentService, ProfessorService, CourseService, EnrollmentService, GradeService, UniversityService
from menus.student_menu import student_menu
from menus.professor_menu import professor_menu
from menus.course_menu import course_menu
from menus.enrollment_menu import enrollment_menu
from menus.grade_menu import grade_menu
from menus.university_menu import university_menu
from utils import configure_logging

def build_services():
    db=Database();db.initialize();db.seed_if_empty()
    student_repo=StudentRepository(db);professor_repo=ProfessorRepository(db);course_repo=CourseRepository(db);enrollment_repo=EnrollmentRepository(db);grade_repo=GradeRepository(db);university_repo=UniversityRepository(db)
    return (
        StudentService(student_repo), ProfessorService(professor_repo),
        CourseService(course_repo,professor_repo), EnrollmentService(enrollment_repo,student_repo,course_repo),
        GradeService(grade_repo,student_repo,course_repo,enrollment_repo), UniversityService(university_repo)
    )

def main():
    configure_logging()
    student,professor,course,enrollment,grade,university=build_services()
    while True:
        print("\n========== Student Management System ==========")
        print("1. Professor Management")
        print("2. Student Management")
        print("3. Course Management")
        print("4. Enrollment Management")
        print("5. Grade Management")
        print("6. University Information")
        print("7. Exit")
        choice=input("Choice: ").strip()
        if choice=="1":professor_menu(professor)
        elif choice=="2":student_menu(student)
        elif choice=="3":course_menu(course)
        elif choice=="4":enrollment_menu(enrollment)
        elif choice=="5":grade_menu(grade)
        elif choice=="6":university_menu(university)
        elif choice=="7":print("Goodbye!");break
        else:print("Invalid choice.")

if __name__=="__main__": main()
