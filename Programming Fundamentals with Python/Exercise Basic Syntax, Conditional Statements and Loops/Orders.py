number_of_orders = int(input())
total_price = 0
for current_order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    needed_capsule_per_day = int(input())
    month_price = price_per_capsule * days * needed_capsule_per_day
    total_price += month_price
    if total_price != 0:
        print(f"The price for the coffee is: ${month_price:.2f}")

print(f"Total: ${total_price:.2f}")
