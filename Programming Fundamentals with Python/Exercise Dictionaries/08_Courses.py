courses = {}
while True:
    command = input()
    if command == "end":
        break
    course_name, student_name = command.split(" : ")
    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)

for course in courses:
    print(f"{course}: {len(courses[course])}")
    for current_student in courses[course]:
        print(f"-- {current_student}")
