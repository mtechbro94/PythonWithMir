def infinite_coffee():
    count = 1
    while True:
        yield f"Refill #{count}"
        count += 1

refill = infinite_coffee()
user2 = infinite_coffee()

for _ in range(5):
    print(next(refill))

for _ in range(6):
    print(next(user2))