from .helpers import run_action

def grade_menu(service):
    while True:
        print("\n===== Grade Management =====\n1. Add\n2. Show All\n3. Show One\n4. Search\n5. Update\n6. Delete\n7. Back")
        ch=input("Choice: ").strip()
        if ch=="1":
            data={"grade_id":input("ID: "),"student_id":input("Student ID: "),"course_id":input("Course ID: "),"score":input("Score 0-20: "),"date":input("Date: ")};run_action(lambda:service.add(data))
        elif ch=="2":
            for g in service.get_all():print(f"{g.grade_id} | Student {g.student} | Course {g.course} | Score {g.score}")
        elif ch=="3":run_action(lambda:show(service.get(input("ID: "))))
        elif ch=="4":
            for g in service.search(input("Student ID or Course ID: ")):print(f"{g.grade_id} | Student {g.student} | Course {g.course} | Score {g.score}")
        elif ch=="5":
            gid=input("ID: ");data={"student_id":input("Student ID: "),"course_id":input("Course ID: "),"score":input("Score: "),"date":input("Date: ")};run_action(lambda:service.update(gid,data))
        elif ch=="6":run_action(lambda:service.delete(input("ID: ")))
        elif ch=="7":return
        else:print("Invalid choice.")
def show(g):print(f"ID: {g.grade_id}\nStudent ID: {g.student}\nCourse ID: {g.course}\nScore: {g.score}\nDate: {g.date}")
