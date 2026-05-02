
coffee_type = "latte"
def update_order():
    coffee_type = "cappuccino"
    def kitchen():
        nonlocal coffee_type
        coffee_type = "mocha"
    kitchen()
    print("After kitchen update", coffee_type)

update_order()