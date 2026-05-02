def pure_coffee(cups):
    return cups * 10

total_coffee = 0

# not recommended
def impure_coffee(cups):
    global total_coffee
    total_coffee += cups


def pour_coffee(n):
    print(n)
    if n == 0:
        return "All cups poured"
    return pour_coffee(n-1)

print(pour_coffee(3))



coffee_types = ["light", "strong", "latte", "strong"]


strong_coffee = list(filter(lambda coffee: coffee!="strong", coffee_types))

print(strong_coffee)