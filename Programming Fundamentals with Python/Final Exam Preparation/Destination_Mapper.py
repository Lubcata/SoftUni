import re
data = input()
pattern = r"(=|\/)([A-Z][A-Za-z]{2,})(\1)"
match = re.findall(pattern, data)

places = []
points = 0
if match:
    for place in match:
        places.append(place[1])
        points += len(place[1])
print(f"Destinations: {', '.join(places)}")
print(f"Travel Points: {points}")