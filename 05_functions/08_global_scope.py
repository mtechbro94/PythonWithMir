coffee_type = "Black"

def front_desk():
    def kitchen():
        global coffee_type
        coffee_type = "Americano"
    kitchen()


front_desk()
print("Final global coffee: ", coffee_type)