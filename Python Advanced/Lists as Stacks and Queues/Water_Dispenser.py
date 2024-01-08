from collections import deque

quantity_of_water = int(input())
collection = deque()

while True:
    name = input()
    if name == "Start":
        break
    collection.append(name)

while True:
    command = input().split()
    if command[0] == "End":
        print(f"{quantity_of_water} liters left")
        break
    if command[0] == "refill":
        quantity_of_water += int(command[1])
    else:
        liters_to_add = int(command[0])
        if quantity_of_water >= liters_to_add:
            quantity_of_water -= liters_to_add
            print(f"{collection.popleft()} got water")
        else:
            print(f"{collection.popleft()} must wait")

