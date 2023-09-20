# · Предпазен найлон - 1.50 лв. за кв. метър
# · Боя - 14.50 лв. за литър
# · Разредител за боя - 5.00 лв. за литър

NYLON_PRICE = 1.50
PAINT_PRICE = 14.50
PAINT_THINNER_PRICE = 5.00
BAG_PRICE = 0.40    

# 1. Необходимо количество найлон (в кв.м.) - цяло число в интервала [1... 100]
# 2. Необходимо количество боя (в литри) - цяло число в интервала [1…100]
# 3. Количество разредител (в литри) - цяло число в интервала [1…30]
# 4. Часовете, за които майсторите ще свършат работата - цяло число в интервала [1…9]

nylon_quantity = int(input())
paint_quantity = int(input())
paint_thinner_quantity = int(input())
work_hours = int(input())

extra_nylon = 2
extra_paint = paint_quantity * 0.10

total_material_price = NYLON_PRICE * (nylon_quantity + extra_nylon) \
    + PAINT_PRICE * (paint_quantity + extra_paint) \
    + PAINT_THINNER_PRICE * paint_thinner_quantity\
    + BAG_PRICE

work_hours_price = total_material_price * 0.30 

total_price = total_material_price + work_hours_price * work_hours
print(total_price)