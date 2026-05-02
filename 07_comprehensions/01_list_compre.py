menu = [
    "Espresso",
    "Iced Coffee",
    "Americano",
    "Cold Brew",
    "Latte"
]

iced_coffee = [my_coffee for my_coffee in menu if "Iced" in my_coffee]

print(iced_coffee)