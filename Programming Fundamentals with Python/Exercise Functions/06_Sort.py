numbers = input().split()
number_list = []

for number in numbers:
    number_list.append(int(number))

print(sorted(number_list))
