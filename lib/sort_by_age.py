def age_sort(student):
    return student[1]
def sort_by_age():
    students = [
    ('Abel', 21),
    ('Bob', 25),
    ('Charlie', 28),
    ('Diana', 27),
    ( 'Eve', 22)
    ]
    sorted_students =sorted(students, key=age_sort)
    return sorted_students
# sorted_students =sort_by_age()
# print(sorted_students)
  