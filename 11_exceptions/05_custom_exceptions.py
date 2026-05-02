def brew_coffee(flavor):
    if flavor not in ["espresso", "latte", "cappuccino"]:
        raise ValueError("Unsupported coffee flavor...")
    print(f"brewing {flavor} coffee...")


brew_coffee("mocha")