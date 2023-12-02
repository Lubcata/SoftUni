def prosper(cities, town, gold):
    if gold < 0:
        print(f"Gold added cannot be a negative number!")
    else:
        cities[town]["gold"] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")
    return cities


def plunder(cities, town, people, gold):
    print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

    cities[town]["population"] -= people
    cities[town]["gold"] -= gold

    if cities[town]["population"] == 0 or cities[town]["gold"] == 0:
        cities.pop(town)
        print(f"{town} has been wiped off the map!")
    return cities


def main():
    cities = {}

    while True:
        city_info = input().split("||")

        city = city_info[0]

        if city == "Sail":
            break

        population = int(city_info[1])
        gold = int(city_info[2])

        if city not in cities.keys():
            cities[city] = {"population": 0, "gold": 0}
        cities[city]["population"] += population
        cities[city]["gold"] += gold

    while True:
        command = input().split("=>")
        event = command[0]
        if event == "End":
            break

        if event == "Plunder":
            # =>{town}=>{people}=>{gold}
            town = command[1]
            people = int(command[2])
            gold = int(command[3])
            plunder(cities, town, people, gold)
        elif event == "Prosper":
            # =>{town}=>{gold}
            town = command[1]
            gold = int(command[2])
            prosper(cities, town, gold)

    if cities:
        print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")

        for town, town_info in cities.items():
            print(f"{town} -> Population: {town_info['population']} citizens, Gold: {town_info['gold']} kg")
    else:
        print("Ahoy, Captain! All targets have been plundered and destroyed!")


main()
