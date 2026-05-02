class BaseCoffee:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} coffee....")

class EspressoCoffee(BaseCoffee):
    def add_flavors(self):
        print("Adding vanilla, caramel.")


class CoffeeShop:
    coffee_cls = BaseCoffee

    def __init__(self):
        self.coffee = self.coffee_cls("Regular")

    def serve(self):
        print(f"Serving {self.coffee.type} coffee in the shop")
        self.coffee.prepare()

class FancyCoffeeShop(CoffeeShop):
    coffee_cls = EspressoCoffee


shop = CoffeeShop()
fancy = FancyCoffeeShop()
shop.serve()
fancy.serve()
fancy.coffee.add_flavors()