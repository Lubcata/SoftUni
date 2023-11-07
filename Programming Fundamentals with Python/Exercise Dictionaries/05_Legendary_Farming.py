items = {"shards": 0, "fragments": 0, "motes": 0}
obtained = False

while not obtained:
    current_item = input().split()
    
    for index in range(0, len(current_item), 2):
        value = int(current_item[index])
        key = current_item[index + 1].lower()
        
        if key not in items:
            items[key] = 0
        items[key] += value
        
        if items["shards"] >= 250:
            print(f"Shadowmourne obtained!")
            items["shards"] -= 250
            obtained = True
        elif items["fragments"] >= 250:
            print(f"Valanyr obtained!")
            items["fragments"] -= 250
            obtained = True
        elif items["motes"] >= 250:
            print(f"Dragonwrath obtained!")
            items["motes"] -= 250
            obtained = True
        if obtained:
            break
for material, quantity in items.items():
    print(f"{material}: {quantity}")