numbers = [float(x)for x in input().split()]
number_dict = {}
for number in numbers:
    if number not in number_dict:
        number_dict[number] = 0
    number_dict[number] += 1

for key, value in number_dict.items():
    print(f"{key} - {value} times")
