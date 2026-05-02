import threading

coffee_stock = 0

def restock():
    global coffee_stock
    for _ in range(100000):
        coffee_stock += 1

threads = [ threading.Thread(target=restock) for _ in range(2)]

for t in threads: t.start()
for t in threads: t.join()

print("Coffee stock: ", coffee_stock)