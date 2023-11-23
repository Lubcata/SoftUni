type_of_fuel = input("Insert fuel type: ")
liters = float(input("Insert fuel: "))
kilometers = float(input("Insert kilometers traveld: "))

cosnumation = liters / kilometers * 100

print(f"Your car consumation is {cosnumation:.2f}/100km. liters of {type_of_fuel}")


