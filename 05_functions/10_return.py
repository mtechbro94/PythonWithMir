# def make_coffee():
#     # return "Here is your espresso"
#     print("Here is your espresso")

# return_value = make_coffee()

# print(return_value)

def idle_barista():
    pass

print(idle_barista())

def sold_cups():
    return 120

total = sold_cups()
print(total)

def coffee_status(cups_left):
    if cups_left == 0:
        return "Sorry, coffee over"
    return "Coffee is ready"
    print("coffee")

print(coffee_status(0))
print(coffee_status(5))


def coffee_report():
    return 100, 20, 10 # sold, remaining

sold, remaining, not_paid = coffee_report()
print("Sold: ", sold)
print("Remaining: ", remaining)