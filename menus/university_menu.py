def university_menu(service):
    for u in service.get_all():
        print(f"ID: {u.university_id}\nName: {u.name}\nCity: {u.city}\nDepartment: {u.department}\nWebsite: {u.website}\n")
