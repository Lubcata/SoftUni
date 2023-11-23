import re


my_string = input()
items = []

while my_string:
    pattern = r"\d+"
    match = re.findall(pattern, my_string)
    if match:
        items.append(match)
    my_string = input()

for item in items:
    print(" ".join(item), end=' ')