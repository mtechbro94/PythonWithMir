class CoffeeOrder:
    
    def __init__(self, type_, size):
        self.type = type_
        self.size = size

    def summary(self):
        return f"{self.size}ml of {self.type} coffee"
    
order = CoffeeOrder("Espresso", 200)
print(order.summary())

order_two = CoffeeOrder("Latte", 220)
print(order_two.summary())