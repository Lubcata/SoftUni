# 1. Бюджетът на Петър - реално число в интервала [1.0…100000.0]
# 2. Броят видеокарти - цяло число в интервала [1…100]
# 3. Броят процесори - цяло число в интервала [1…100]
# 4. Броят рам памет - цяло число в интервала [1…100]

budget = float(input())
video_card_count = int(input())
processor_count = int(input())
ram_count = int(input())

# · Видеокарта – 250 лв./бр.
# · Процесор – 35% от цената на закупените видеокарти/бр.
# · Рам памет – 10% от цената на закупените видеокарти/бр.

video_card_price = 250
processor_price = (video_card_count * video_card_price) * 0.35
ram_price = (video_card_count * video_card_price) * 0.10

# · Ако бюджета е достатъчен:
#     "You have {остатъчен бюджет} leva left!"
# · Ако сумата надхвърля бюджета:
#     "Not enough money! You need {нужна сума} leva more!"
# Резултатът да се форматира до втория знак след десетичната запетая.
items_price = video_card_count * video_card_price + \
            processor_count * processor_price + \
            ram_count * ram_price 

if video_card_count > processor_count:
    items_price = items_price - (items_price * 0.15)

if budget >= items_price:
    print(f"You have {budget - items_price :.2f} leva left!")
else:
    print(f"Not enough money! You need {items_price - budget :.2f} leva more!")