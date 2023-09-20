# • Пакет химикали - 5.80 лв.
# • Пакет маркери - 7.20 лв.
# • Препарат - 1.20 лв (за литър)

PENS_PRICE = 5.80
MARKERS_PRICE = 7.20
CLEANING_MATERIALS_PRICE = 1.20

# · Брой пакети химикали - цяло число в интервала [0...100]
# · Брой пакети маркери - цяло число в интервала [0...100]
# · Литри препарат за почистване на дъска - цяло число в интервала [0…50]
# · Процент намаление - цяло число в интервала [0...100]

pens_count = int(input())
markers_count = int(input())
cleaning_materials_liters = int(input())
discount_percent = int(input()) / 100

money_needed = PENS_PRICE * pens_count\
               + MARKERS_PRICE * markers_count\
               + CLEANING_MATERIALS_PRICE * cleaning_materials_liters
money_needed_with_discound = money_needed - (money_needed * discount_percent)
print(money_needed_with_discound)