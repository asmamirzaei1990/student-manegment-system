STUDENTS_DATA = [
    (f"S{i:03}", ["Amir", "Sara", "Reza", "Neda", "Ali", "Maryam", "Hassan", "Leila", "Arman", "Shirin"][ (i-1)%10 ],
     ["Hosseini", "Ahmadi", "Karimi", "Moradi", "Mohammadi", "Rahimi", "Ebrahimi", "Ahmadi", "Rahimi", "Ghasemi"][ (i-1)%10 ],
     20 + (i % 5), ["Tehran", "Shiraz", "Tabriz", "Isfahan", "Mashhad", "Rasht", "Kerman", "Sanandaj", "Qom", "Yazd"][ (i-1)%10 ],
     ["Computer Science", "Software Engineering", "Computer Engineering"][ (i-1)%3 ], 2 + (i % 7),
     f"student{i:03}@example.com", f"0913000{i:04}", round(15.0 + ((i * 37) % 50) / 10, 1))
    for i in range(1, 51)
]
