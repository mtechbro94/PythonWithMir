class Coffeecup:
    size = 150 #ml

    def describe(self):
        return f"A {self.size}ml coffee cup"
    

cup = Coffeecup()
print(cup.describe())
print(Coffeecup.describe(cup))

cup_two = Coffeecup()
cup_two.size = 100
print(Coffeecup.describe(cup_two))