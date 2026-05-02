class InvalidCoffeeError(Exception): pass

def bill(flavor, cups):
    menu = {"espresso": 20, "latte": 40}
    try:
        if flavor not in menu:
            raise InvalidCoffeeError("that coffee is not available")
        if not isinstance(cups, int):
            raise TypeError("Number of cups must be an integer")
        total = menu[flavor] * cups
        print(f"Your bill for {cups} cups of {flavor} coffee: rupees {total}")
    except Exception as e:
        print("Error: ", e)
    finally:
        print("Thank you for visiting codewithcoffee!")


bill("mocha", 2)
bill("espresso", "three")
bill("latte", 3)