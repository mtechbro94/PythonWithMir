class OutOfIngredientsError(Exception):
    pass

def make_coffee(milk, sugar):
    if milk == 0 or sugar == 0:
        raise OutOfIngredientsError("Missing milk or sugar")
    print("coffee is ready...")


make_coffee(0, 1)