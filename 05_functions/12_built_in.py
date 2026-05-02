def coffee_flavor(flavor="espresso"):
    """Return the flavor of coffee."""
    coffee="latte"
    return flavor


print(coffee_flavor.__doc__)
print(coffee_flavor.__name__)

help(len)

def generate_bill(coffee=0, samosa=0):
    """
    Calculate the total bill for coffee and samosa

    :param coffee: Number of coffee cups (10 rupees each)
    :param samosa: NUmber of samosa (15 rupees each)
    : return: (total amount, thank you message as string)
    """
    total = coffee*10 + samosa*15
    return total, "Thank you for visiting codewithcoffee.com"