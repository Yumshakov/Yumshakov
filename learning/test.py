def cakes(recipe, available):
    lst = []
    for key in recipe.keys():
        lst.append(available[key]//recipe[key])
    return min(lst)

print(cakes({'flour': 500, 'sugar': 200, 'eggs': 1},
      {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}))
