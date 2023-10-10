numbers = input().split()
number_list = []

for number in numbers:
    number_list.append(int(number))

min_number = min(number_list)
max_number = max(number_list)
sum_numbers = sum(number_list)
print(f"The minimum number is {min_number}")
print(f"The maximum number is {max_number}")
print(f"The sum number is: {sum_numbers}")
