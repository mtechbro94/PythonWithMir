def coffee_customer():
    print("Welcome ! What coffee would you like ?")
    order = yield
    while True:
        print(f"Preparing: {order}")
        order = yield

stall = coffee_customer()
next(stall) # start the generator

stall.send("Espresso")
stall.send("Cold Brew")