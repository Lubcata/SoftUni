def cookbook(*recipes):
    recipes_by_cuisine = {}

    for recipe in recipes:
        name, cuisine, ingredients = recipe
        if cuisine not in recipes_by_cuisine:
            recipes_by_cuisine[cuisine] = []
        recipes_by_cuisine[cuisine].append((name, ingredients))

    sorted_cuisines = sorted(recipes_by_cuisine.items(), key=lambda x: (-len(x[1]), x[0]))

    output = ""

    for cuisine, recipes in sorted_cuisines:
        output += f"{cuisine} cuisine contains {len(recipes)} recipes:\n"

        sorted_recipes = sorted(recipes, key=lambda x: x[0])

        for recipe_name, ingredients in sorted_recipes:
            ingredients_str = ", ".join(ingredients)
            output += f"  * {recipe_name} -> Ingredients: {ingredients_str}\n"

    return output


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))
