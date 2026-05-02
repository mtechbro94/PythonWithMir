class Coffee:
    temperature = "hot"
    strength = "Strong"


cutting = Coffee()
print(cutting.temperature)

cutting.temperature = "Mild"
cutting.cup = "small"
print("After changing ",cutting.temperature)
print("cup size is  ",cutting.cup)
print("Direct look into the class ", Coffee.temperature)

del cutting.temperature
del cutting.cup
print(cutting.temperature)
print(cutting.cup)