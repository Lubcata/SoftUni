# · Ако числото е до 100 включително, бонус точките са 5;
# · Ако числото е по-голямо от 100, бонус точките са 20% от числото;
# · Ако числото е по-голямо от 1000, бонус точките са 10% от числото.

# o За четно число à + 1 т.
# o За число, което завършва на 5 à + 2 т.

starting_number = int(input())

if starting_number <= 100:
    bonus_points = 5
elif starting_number <= 1000:
    bonus_points = starting_number * 0.20
else:
    bonus_points = starting_number * 0.10

extra_bonus_points = 0

if starting_number % 2 == 0:
    extra_bonus_points = 1

if starting_number % 10 == 5:
    extra_bonus_points = 2

print(bonus_points + extra_bonus_points)
print(starting_number + bonus_points + extra_bonus_points)