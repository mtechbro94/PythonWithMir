class Coffee:
    def __init__(self, sweetness, milk_level):
        self.sweetness = sweetness
        self.milk_level = milk_level

    def sip(self):
        print("Sipping coffee")

    def add_sugar(self, amount):
        print("added the sugar")

my_coffee = Coffee(sweetness=3, milk_level=2)

my_coffee.add_sugar(3)