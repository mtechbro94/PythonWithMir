coffee_order = dict(type="Espresso", size="Large", sugar=2)
print(f"Coffee order: {coffee_order}")

coffee_recipe = {}
coffee_recipe["base"] = "coffee grounds"
coffee_recipe["liquid"] = "milk"

print(f"Recipe base: {coffee_recipe['base']}")
print(f"Recipe: {coffee_recipe}")
del coffee_recipe["liquid"]
print(f"Recipe: {coffee_recipe}")

print(f"Is sugar in the order? {'sugar' in coffee_order}")

coffee_order = {"type": "Latte", "size": "Medium", "sugar": 1}

# print(f"Order details (keys): {coffee_order.keys()}")
# print(f"Order details (values): {coffee_order.values()}")
# print(f"Order details (items): {coffee_order.items()}")

last_item = coffee_order.popitem()
print(f"Removed last item: {last_item}")

extra_ingredients = {"syrup": "vanilla", "milk": "almond"}
coffee_recipe.update(extra_ingredients)

print(f"Updated coffee recipe: {coffee_recipe}")

customer_note = coffee_order.get("size", "NO Note")
print(f"customer_note is: {customer_note}")