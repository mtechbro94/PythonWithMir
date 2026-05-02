class CoffeeOrder:
    def __init__(self, coffee_type, sweetness, size):
        self.coffee_type = coffee_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data["coffee_type"],
            order_data["sweetness"],
            order_data["size"],
        )
    
    @classmethod
    def from_string(cls, order_string):
        coffee_type, sweetness, size = order_string.split("-")
        return cls(coffee_type, sweetness, size)
    
class CoffeeUtils:
    @staticmethod
    def is_valid_size(size):
        return size in ["Small", "Medium", "Large"]


print(CoffeeUtils.is_valid_size("Medium"))

order1 = CoffeeOrder.from_dict({"coffee_type": "espresso", "sweetness": "medium", "size":"Large"})

order2 = CoffeeOrder.from_string("Latte-Low-Small")

order3 = CoffeeOrder("Large", "Low", "Large")

print(order1.__dict__)
print(order2.__dict__)
print(order3.__dict__)