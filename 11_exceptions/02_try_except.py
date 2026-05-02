coffee_menu = {"espresso": 30, "latte": 40}

try:
    coffee_menu["cappuccino"]
except KeyError:
    print("The key that you are tying to access does not exists")


print("Hello coffee code")