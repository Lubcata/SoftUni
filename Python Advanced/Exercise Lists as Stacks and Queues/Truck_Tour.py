from collections import deque

number_of_pumps = int(input())
pumps = deque([int(x) for x in input().split()] for _ in range(number_of_pumps))

gas_in_tank = 0

pumps_copy = pumps.copy()
index_counter = 0

while pumps_copy:
    petrol, distance = pumps_copy.popleft()
    gas_in_tank += petrol
    if gas_in_tank >= distance:
        gas_in_tank -= distance
    else:
        pumps.rotate(-1)
        pumps_copy = pumps.copy()
        index_counter += 1
        gas_in_tank = 0

print(index_counter)