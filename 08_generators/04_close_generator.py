def local_coffee():
    yield "Espresso"
    yield "Latte"

def imported_coffee():
    yield "Americano"
    yield "Cappuccino"

def full_menu():
    yield from local_coffee()
    yield from imported_coffee()

for coffee in full_menu():
    print(coffee)


def coffee_stall():
    try:
        while True:
            order = yield "Waiting for coffee order"
    except:
        print("Stall closed, No more coffee")


stall = coffee_stall()
print(next(stall))
stall.close() #cleanup