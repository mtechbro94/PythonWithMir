coffee_type = "Latte"
customer_name = "Priya"

print(f"Order for {customer_name} : {coffee_type} please !")

coffee_description = "Rich and Smooth"
print(f"First word: {coffee_description[:4]}")
print(f"Last word: {coffee_description[8:]}")
print(f"Last word: {coffee_description[::-1]}")

label_text = "Café Spécial"
ecoded_label = label_text.encode("utf-8")
print(f"Non Encoded label: {label_text}")
print(f"Encoded label: {ecoded_label}")
decoded_label = ecoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}")