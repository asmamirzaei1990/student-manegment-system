from .helpers import run_action

def enrollment_menu(service):
    while True:
        print("\n===== Enrollment Management =====\n1. Add\n2. Show All\n3. Show One\n4. Search\n5. Update\n6. Delete\n7. Back")
        ch=input("Choice: ").strip()
        if ch=="1":
            data={"enrollment_id":input("ID: "),"student_id":input("Student ID: "),"course_id":input("Course ID: "),"enrollment_date":input("Date YYYY-MM-DD: "),"status":input("Status: ") or "Active"};run_action(lambda:service.add(data))
        elif ch=="2":
            for e in service.get_all():print(f"{e.enrollment_id} | Student {e.student} | Course {e.course} | {e.status}")
        elif ch=="3":run_action(lambda:show(service.get(input("ID: "))))
        elif ch=="4":
            for e in service.search(input("Student ID or Course ID: ")):print(f"{e.enrollment_id} | Student {e.student} | Course {e.course} | {e.status}")
        elif ch=="5":
            eid=input("ID: ");data={"student_id":input("Student ID: "),"course_id":input("Course ID: "),"enrollment_date":input("Date: "),"status":input("Status: ")};run_action(lambda:service.update(eid,data))
        elif ch=="6":run_action(lambda:service.delete(input("ID: ")))
        elif ch=="7":return
        else:print("Invalid choice.")
def show(e):print(f"ID: {e.enrollment_id}\nStudent ID: {e.student}\nCourse ID: {e.course}\nDate: {e.enrollment_date}\nStatus: {e.status}")
