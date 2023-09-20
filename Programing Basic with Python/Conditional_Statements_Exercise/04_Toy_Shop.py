# · Пъзел - 2.60 лв.
# · Говореща кукла - 3 лв.
# · Плюшено мече - 4.10 лв.
# · Миньон - 8.20 лв.
# · Камионче - 2 лв.

PUZZEL_PRICE = 2.60
TALKING_DOLL_PRICE = 3.00
TEDDY_BEAR_PRICE = 4.10
MINION_PRICE = 8.20
TRUCK_PRICE = 2.00

# 1. Цена на екскурзията - реално число в интервала [1.00 … 10000.00]
# 2. Брой пъзели - цяло число в интервала [0… 1000]
# 3. Брой говорещи кукли - цяло число в интервала [0 … 1000]
# 4. Брой плюшени мечета - цяло число в интервала [0 … 1000]
# 5. Брой миньони - цяло число в интервала [0 … 1000]
# 6. Брой камиончета - цяло число в интервала [0 … 1000]

vacation_price = float(input())
puzzel_count = int(input())
talking_doll_count = int(input())
teddy_bear_count = int(input())
minion_count = int(input())
truck_coint = int(input())

toys_price = puzzel_count + talking_doll_count + teddy_bear_count + minion_count + truck_coint
discount = 0
if toys_price >= 50:
    discount = 0.25

total_income = puzzel_count * PUZZEL_PRICE \
            + talking_doll_count * TALKING_DOLL_PRICE \
            + teddy_bear_count * TEDDY_BEAR_PRICE\
            + minion_count * MINION_PRICE\
            + truck_coint * TRUCK_PRICE

total_income_with_discount = total_income * (1 - discount)
rent_cost = total_income_with_discount * 0.10

final_income = total_income_with_discount - rent_cost

if final_income >= vacation_price:
    print(f"Yes! {final_income - vacation_price :.2f} lv left.")
else:
    print(f"Not enough money! {vacation_price - final_income :.2f} lv needed.")