number_of_students = int(input())

students = {}

for student in range(number_of_students):
    name, grade = input().split()
    grade_float = float(grade)

    if name not in students:
        students[name] = []
    students[name].append(grade_float)

for student, grades in students.items():
    average_grade = sum(grades) / len(grades)
    formatted_grade = " ".join(f"{grade:.2f}" for grade in grades)
    print(f"{student} -> {formatted_grade} (avg: {average_grade:.2f})")