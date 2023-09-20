# • Пилешко меню – 10.35 лв.
# • Меню с риба – 12.40 лв.
# • Вегетарианско меню – 8.15 лв.

CHICKEN_MEET = 10.35
FISH_MENU = 12.40
VEGETARIAN_MENU = 8.15

delivery = 2.5

# · Брой пилешки менюта – цяло число в интервала [0 … 99]
# · Брой менюта с риба – цяло число в интервала [0 … 99]
# · Брой вегетариански менюта – цяло число в интервала [0 … 99]

chicken_meet_quantity = int(input())
fish_menu_quantity = int(input())
vegetarian_menu_quantity = int(input())

menu_price = CHICKEN_MEET * chicken_meet_quantity \
    + FISH_MENU * fish_menu_quantity \
    + VEGETARIAN_MENU * vegetarian_menu_quantity

dessert_price = menu_price * 0.20
total_price = menu_price + dessert_price + delivery

print(total_price)