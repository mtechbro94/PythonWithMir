# file = open("order.txt", "w")
# try:
#     file.write("Espresso coffee - 2 cups")
# finally:
#     file.close()


with open("order.txt", "w") as file:
    file.write("latte coffee - 4 cups")