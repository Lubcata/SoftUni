import re

command = input()

bought_furnitures = []
total_cost = 0
pattern = r">>([a-zA-Z]+)<<(\d+\.?\d*)!(\d+)"

while command != "Purchase":
    
    match = re.search(pattern, command)
    if match:
        furniture, price, quantity = match.groups()
        bought_furnitures.append(furniture)
        total_cost += float(price) * int(quantity)
    command = input()
    
print("Bought furniture:")
for furniture in bought_furnitures:
    print(furniture)
print(f"Total money spend: {total_cost:.2f}")
    
    