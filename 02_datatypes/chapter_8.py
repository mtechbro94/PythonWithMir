ingredients = ["water", "milk", "coffee grounds"]
ingredients.append("sugar")
print(f"Ingredients are: {ingredients}")
ingredients.remove("water")
print(f"Ingredients are: {ingredients}")

flavor_options = ["vanilla", "caramel"]
coffee_ingredients = ["water", "milk"]

coffee_ingredients.extend(flavor_options)
print(f"coffee: {coffee_ingredients}")
coffee_ingredients.insert(2, "coffee grounds")
print(f"coffee: {coffee_ingredients}")

last_added = coffee_ingredients.pop()
print(f"{last_added}")
print(f"coffee: {coffee_ingredients}")
coffee_ingredients.reverse()
print(f"coffee: {coffee_ingredients}")
coffee_ingredients.sort()
print(f"coffee: {coffee_ingredients}")

sugar_levels = [1, 2, 3, 4, 5]
print(f"Maximum sugar level: {max(sugar_levels)}")
print(f"Minimum sugar level: {min(sugar_levels)}")

base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]

full_liquid_mix = base_liquid + extra_flavor
print(f"Liquid mix: {full_liquid_mix}")

strong_brew = ["black tea", "water"] * 3
print(f"String brew: {strong_brew}")

raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(f"Bytes: {raw_spice_data}")