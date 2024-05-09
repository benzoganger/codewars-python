def cakes(recipe, available):
    required_ingredients = list(recipe.keys())
    if not all(ingr in available for ingr in required_ingredients):
        return 0

    canBake = []
    for ingr in required_ingredients:
        if recipe[ingr] == 0:
            return 0

        if available[ingr] >= recipe[ingr]:
            canBake.append(available[ingr] // recipe[ingr])
        else:
            return 0

    return min(canBake)
