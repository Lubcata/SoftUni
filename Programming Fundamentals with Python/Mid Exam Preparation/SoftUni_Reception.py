from math import ceil

total_employee_efficiency = 0
needed_hours = 0
for _ in range(3):
    employee_efficiency = int(input())
    total_employee_efficiency += employee_efficiency
    if employee_efficiency >= 100:
        break
count_of_students = int(input())
if count_of_students > 0:
    needed_hours = ceil(count_of_students / total_employee_efficiency)

    for hour in range(1, needed_hours + 1):
        if hour % 4 == 0:
            needed_hours += 1

print(f"Time needed: {needed_hours}h.")

