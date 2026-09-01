from .helpers import run_action

def course_menu(service):
    while True:
        print("\n===== Course Management =====\n1. Add\n2. Show All\n3. Show One\n4. Search\n5. Update\n6. Delete\n7. Back")
        ch=input("Choice: ").strip()
        if ch=="1":
            data={"course_id":input("ID: "),"name":input("Name: "),"units":input("Units: "),"teacher_id":input("Professor ID: "),"capacity":input("Capacity: "),"semester":input("Semester: "),"department":input("Department: "),"day":input("Day: "),"start_time":input("Start: "),"end_time":input("End: "),"room":input("Room: ")};run_action(lambda:service.add(data))
        elif ch=="2":
            for c in service.get_all():print(f"{c.course_id} | {c.name} | {c.units} units | Teacher {c.teacher} | Capacity {c.capacity}")
        elif ch=="3":run_action(lambda:show(service.get(input("ID: "))))
        elif ch=="4":
            for c in service.search(input("Name: ")):print(f"{c.course_id} | {c.name} | Teacher {c.teacher}")
        elif ch=="5":
            cid=input("ID: ");data={"name":input("Name: "),"units":input("Units: "),"teacher_id":input("Professor ID: "),"capacity":input("Capacity: "),"semester":input("Semester: "),"department":input("Department: "),"day":input("Day: "),"start_time":input("Start: "),"end_time":input("End: "),"room":input("Room: ")};run_action(lambda:service.update(cid,data))
        elif ch=="6":run_action(lambda:service.delete(input("ID: ")))
        elif ch=="7":return
        else:print("Invalid choice.")
def show(c):print(f"ID: {c.course_id}\nName: {c.name}\nUnits: {c.units}\nTeacher ID: {c.teacher}\nCapacity: {c.capacity}\nSemester: {c.semester}\nDepartment: {c.department}\nSchedule: {c.day} {c.start_time}-{c.end_time}\nRoom: {c.room}")
