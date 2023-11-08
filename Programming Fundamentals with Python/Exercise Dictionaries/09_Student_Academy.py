
count_of_students = int(input())
students = {}
for student in range(count_of_students):
    student_name = input()
    student_grade = float(input())
    if student not in students:
        students[student_name] = 0
    students[student_name] += student_grade

print(students)