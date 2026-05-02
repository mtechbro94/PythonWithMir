# coffee = "Latte"

# def prepare_coffee(order):
#     print("Preparing ", order)


# prepare_coffee(coffee)
# print(coffee)


coffee = [1, 2, 3]

def edit_coffee(cup):
    cup[1] = 42

edit_coffee(coffee)
print(coffee)


def make_coffee(tea, milk, sugar):
    print(tea, milk, sugar)

make_coffee("Arabica", "Yes", "Low") #positional
make_coffee(tea="Robusta", sugar="Medium", milk="No") #keywords


def special_coffee(*ingredients, **extras):
    print("Ingredients", ingredients)
    print("Extras", extras)

special_coffee("Vanilla", "Caramel", sweetener="Honey", foam="yes")

# def coffee_order(order=[]):
#     order.append("Espresso")
#     print(order)

def coffee_order(order=None):
    if order is None:
        order = []
    print(order)

coffee_order()
coffee_order()