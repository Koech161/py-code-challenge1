def sort_by_age():
    students = [
    ('Abel', 21),
    ('Bob', 25),
    ('Charlie', 28),
    ('Diana', 27),
    ('Eve', 22)
    ]
    sorted_students =sorted(students, key=lambda student:student[1])
    return sorted_students
sorted_students =sort_by_age()
print(sorted_students)
  