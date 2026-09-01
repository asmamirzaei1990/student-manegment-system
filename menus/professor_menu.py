from .helpers import run_action

def professor_menu(service):
    while True:
        print("\n===== Professor Management =====\n1. Add\n2. Show All\n3. Show One\n4. Search\n5. Update\n6. Delete\n7. Back")
        ch=input("Choice: ").strip()
        if ch=="1":
            data={"professor_id":input("ID: "),"first_name":input("First name: "),"last_name":input("Last name: "),"age":input("Age: "),"phone":input("Phone: "),"email":input("Email: "),"degree":input("Degree: "),"specialization":input("Specialization: "),"department":input("Department: "),"employment_type":input("Employment type: ")};run_action(lambda:service.add(data))
        elif ch=="2":
            for p in service.get_all():print(f"{p.professor_id} | {p.full_name} | {p.specialization} | {p.department}")
        elif ch=="3":run_action(lambda:show(service.get(input("ID: "))))
        elif ch=="4":
            for p in service.search(input("Name: ")):print(f"{p.professor_id} | {p.full_name} | {p.specialization}")
        elif ch=="5":
            pid=input("ID: ");data={"first_name":input("First name: "),"last_name":input("Last name: "),"age":input("Age: "),"phone":input("Phone: "),"email":input("Email: "),"degree":input("Degree: "),"specialization":input("Specialization: "),"department":input("Department: "),"employment_type":input("Employment type: ")};run_action(lambda:service.update(pid,data))
        elif ch=="6":run_action(lambda:service.delete(input("ID: ")))
        elif ch=="7":return
        else:print("Invalid choice.")
def show(p):print(f"ID: {p.professor_id}\nName: {p.full_name}\nAge: {p.age}\nDegree: {p.degree}\nSpecialization: {p.specialization}\nDepartment: {p.department}\nEmployment: {p.employment_type}")
