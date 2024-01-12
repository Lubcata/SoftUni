from collections import deque

quantity_of_food = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))

while orders:
    if orders[0] <= quantity_of_food:
        current_order = orders.popleft()
        quantity_of_food -= current_order
    else:
        break
if orders:
    print("Orders left:", *orders)
else:
    print("Orders complete")
