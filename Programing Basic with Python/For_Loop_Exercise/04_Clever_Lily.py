
age = int(input())
washing_machine = float(input())
toy_price = int(input())

total_money = 0
for birthday in range(1, age + 1):
    if birthday % 2 == 0:
        total_money += birthday * 5
        total_money -= 1
    else:
        total_money += toy_price

if total_money >= washing_machine:
    print(f"Yes! {total_money - washing_machine :.2f}")
else:
    print(f"No! {washing_machine - total_money :.2f}")