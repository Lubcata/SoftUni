number_of_cars = int(input())

cars = set()

for car in range(number_of_cars):
    direction, car_number = input().split(", ")

    if direction == "IN":
        cars.add(car_number)
    elif direction == "OUT":
        if car_number in cars:
            cars.remove(car_number)
if cars:
    for car in cars:
        print(car)
else:
    print("Parking Lot is Empty")