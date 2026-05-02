def process_order(item, quantity):
    try:
        price = {"espresso": 20}[item]
        cost = price * quantity
        print(f"total cost is {cost}")
    except KeyError:
        print("Sorry that coffee is not on menu")
    except TypeError:
        print("Quantity must be in number")

process_order("latte", 2)
process_order("espresso", "two")