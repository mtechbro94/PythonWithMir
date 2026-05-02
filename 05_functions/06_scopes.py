def serve_coffee():
    coffee_type = "Espresso" # local scope
    print(f"Inside function {coffee_type}")


coffee_type = "Americano"
serve_coffee()
print(f"Outside function: {coffee_type}")


def coffee_counter():
    coffee_order = "latte" # Enclosing scope
    def print_order():
        coffee_order = "Cappuccino"
        print("Inner:", coffee_order)
    print_order()
    print("Outer: ", coffee_order)

coffee_order = "Mocha" # Global
coffee_counter()
print("Global :", coffee_order)