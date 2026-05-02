class Coffee:
    origin = "Ethiopia"

print(Coffee.origin)

Coffee.is_hot = True
print(Coffee.is_hot)

# creating objects from class Coffee

espresso = Coffee()
print(f"Espresso {espresso.origin}")
print(f"Espresso {espresso.is_hot}")
espresso.is_hot = False

print("Class: ", Coffee.is_hot)
print(f"Espresso {espresso.is_hot}")
espresso.flavor = "Espresso"
print(espresso.flavor)