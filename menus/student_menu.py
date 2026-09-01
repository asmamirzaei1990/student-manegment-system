from models import Student
from .helpers import run_action

def student_menu(service):
    while True:
        print("\n===== Student Management =====")
        print("1. Add  2. Show All  3. Show One  4. Search  5. Update  6. Delete  7. Back")
        choice=input("Choice: ").strip()
        if choice=="1":
            def action():
                service.add(dict(student_id=input("ID: "),first_name=input("First name: "),last_name=input("Last name: "),age=input("Age: "),birth_place=input("Birth place: "),major=input("Major: "),semester=input("Semester: "),email=input("Email: "),phone=input("Phone: "),gpa=input("GPA: ")))
                print("Student added successfully.")
            run_action(action)
        elif choice=="2":
            for s in service.get_all(): print(f"{s.student_id} | {s.full_name} | {s.major} | GPA {s.gpa}")
        elif choice=="3":
            run_action(lambda: print_student(service.get(input("ID: "))))
        elif choice=="4":
            for s in service.search(input("Name: ")): print(f"{s.student_id} | {s.full_name} | {s.major} | GPA {s.gpa}")
        elif choice=="5":
            sid=input("ID: ")
            data={"first_name":input("First name: "),"last_name":input("Last name: "),"age":input("Age: "),"birth_place":input("Birth place: "),"major":input("Major: "),"semester":input("Semester: "),"email":input("Email: "),"phone":input("Phone: "),"gpa":input("GPA: ")}
            run_action(lambda: service.update(sid,data))
        elif choice=="6": run_action(lambda: service.delete(input("ID: ")))
        elif choice=="7": return
        else: print("Invalid choice.")

def print_student(s):
    print(f"ID: {s.student_id}\nName: {s.full_name}\nAge: {s.age}\nBirth place: {s.birth_place}\nMajor: {s.major}\nSemester: {s.semester}\nEmail: {s.email}\nPhone: {s.phone}\nGPA: {s.gpa}")
