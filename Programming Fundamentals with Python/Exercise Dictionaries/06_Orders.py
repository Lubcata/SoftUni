products = {}

while True:
    commands = input()
    if commands == "buy":
        break

    product, price, quantity = commands.split()
    quantity = int(quantity)
    price = float(price)
    if product not in products.keys():
        products[product] = [price, quantity]
    else:
        products[product][0] = price
        products[product][1] += quantity

for product, details in products.items():
    total_cost = details[0] * details[1]
    print(f"{product} -> {total_cost:.2f}")
