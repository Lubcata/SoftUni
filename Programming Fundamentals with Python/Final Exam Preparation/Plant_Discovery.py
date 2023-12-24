class PlantExhibition:
    def __init__(self):
        self.plants = {}

    def add_plant(self, plant, rarity):
        self.plants[plant] = {"rarity": rarity, "ratings": []}

    def rate_plant(self, plant, rating):
        if plant in self.plants:
            self.plants[plant]["ratings"].append(rating)
        else:
            print("error")

    def update_rarity(self, plant, new_rarity):
        if plant in self.plants:
            self.plants[plant]["rarity"] = new_rarity
        else:
            print("error")

    def reset_ratings(self, plant):
        if plant in self.plants:
            self.plants[plant]["ratings"] = []
        else:
            print("error")

    def exhibition(self):
        print("Plants for the exhibition:")
        for plant, data in self.plants.items():
            rarity = data["rarity"]
            ratings = data["ratings"]

            if ratings:
                average_rating = sum(ratings) / len(ratings)
            else:
                average_rating = 0

            print(f"- {plant}; Rarity: {rarity}; Rating: {average_rating:.2f}")


def main():
    n = int(input())
    exhibition = PlantExhibition()

    for _ in range(n):
        data = input().split("<->")
        plant, rarity = data[0], int(data[1])
        exhibition.add_plant(plant, rarity)

    command = input()

    while command != "Exhibition":
        tokens = command.split(" ")
        action, plant = tokens[0], tokens[1]

        if action == "Rate:":
            try:
                rating = int(tokens[-1])
                exhibition.rate_plant(plant, rating)
            except ValueError:
                print("error")
        elif action == "Update:":
            try:
                new_rarity = int(tokens[-1])
                exhibition.update_rarity(plant, new_rarity)
            except ValueError:
                print("error")
        elif action == "Reset:":
            exhibition.reset_ratings(plant)
        else:
            print("error")

        command = input()

    exhibition.exhibition()


if __name__ == "__main__":
    main()
