from collections import deque

amount_of_money = [int(x) for x in input().split()]
prices_of_food = deque([int(x) for x in input().split()])

eaten_food = 0

while amount_of_money and prices_of_food:
    money = amount_of_money[-1]
    price = prices_of_food[0]

    if money == price:
        amount_of_money.pop()
        prices_of_food.popleft()
        eaten_food += 1
    elif money >= price:
        amount_of_money.pop()
        prices_of_food.popleft()

        eaten_food += 1

        change = money - price
        if amount_of_money:
            amount_of_money[-1] += change
    elif money < price:
        amount_of_money.pop()
        prices_of_food.popleft()

if eaten_food >= 4:
    print(f"Gluttony of the day! Henry ate {eaten_food} foods.")
elif 0 < eaten_food < 4:
    if eaten_food == 1:
        print(f"Henry ate: {eaten_food} food.")
    else:
        print(f"Henry ate: {eaten_food} foods.")
else:
    print("Henry remained hungry. He will try next weekend again.")
