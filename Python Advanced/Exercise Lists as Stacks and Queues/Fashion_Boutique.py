from collections import deque

clothes = deque([int(x) for x in input().split()])
capacity_of_rack = int(input())
rack_counter = 1
current_rack = capacity_of_rack


while clothes:
    current_cloth = clothes.pop()
    if current_rack >= current_cloth:
        current_rack -= current_cloth
    else:
        rack_counter += 1
        current_rack = capacity_of_rack - current_cloth
print(rack_counter)
