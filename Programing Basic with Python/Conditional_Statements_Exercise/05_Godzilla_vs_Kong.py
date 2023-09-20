# Ред 1. Бюджет за филма – реално число в интервала [1.00 … 1000000.00]
# Ред 2. Брой на статистите – цяло число в интервала [1 … 500]
# Ред 3. Цена за облекло на един статист – реално число в интервала [1.00 … 1000.00]

budget = float(input())
walk_count = int(input())
walk_dress_price = float(input())

# Декорът за филма е на стойност 10% от бюджета.
# При повече от 150 статиста, има отстъпка за облеклото на стойност 10%.
discount_dress = walk_dress_price * 0.10
decor_price = budget * 0.10
if walk_count > 150:
    walk_dress_price -= discount_dress

# · Ако парите за декора и дрехите са повече от бюджета:
#     o "Not enough money!"
#     o "Wingard needs {парите недостигащи за филма} leva more."
# · Ако парите за декора и дрехите са по малко или равни на бюджета:
#     o "Action!"
#     o "Wingard starts filming with {останалите пари} leva left."

# Резултатът трябва да е форматиран до втория знак след десетичната запетая.

money_needed = decor_price + walk_count * walk_dress_price
enough_money = budget - money_needed
not_enough_money = money_needed - budget

if money_needed > budget:
    print(f"Not enough money!\nWingard needs {not_enough_money :.2f} leva more.")
else:
    print(f"Action!\nWingard starts filming with {enough_money :.2f} leva left.")