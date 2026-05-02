def serve_coffee(flavor):
    try:
        print(f"Preparing {flavor} coffee...")
        if flavor == "unknown":
            raise ValueError("We don't know that flavor")
    except ValueError as e:
        print("Error: ", e)
    else:
        print(f"{flavor} coffee is served")
    finally:
        print("Next customer please")

serve_coffee("espresso")
serve_coffee("unknown")