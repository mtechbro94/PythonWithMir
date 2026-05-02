favourite_coffees = [
    "Espresso", "Americano", "Espresso",
    "Cold Brew", "Americano", "Cappuccino"
]

unique_coffee = {coffee for coffee in favourite_coffees }
print(unique_coffee)


recipes = {
    "Espresso": ["espresso beans", "water"],
    "Cappuccino": ["espresso", "milk", "foam"],
    "Latte": ["espresso", "steamed milk"],
}

unique_ingredients = {ingredient for ingredients in recipes.values() for ingredient in ingredients}

print(unique_ingredients)