def serve_coffee():
    yield "Cup 1: Espresso"
    yield "Cup 2: Latte"
    yield "Cup 3: Cappuccino"

stall = serve_coffee()

# for cup in stall:
#     print(cup)

def get_coffee_list():
    return ["Cup 1", "Cup 2", "Cup 3"]

# generator function
def get_coffee_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

coffee = get_coffee_gen()
print(next(coffee))
print(next(coffee))
print(next(coffee))
# print(next(coffee)) # gives error