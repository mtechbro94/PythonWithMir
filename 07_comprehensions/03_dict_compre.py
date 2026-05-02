coffee_prices_inr = {
    "Espresso": 40,
    "Americano": 50,
    "Cold Brew": 200
}

coffee_prices_usd = {coffee:price / 80 for coffee, price in coffee_prices_inr.items()}
print(coffee_prices_usd)