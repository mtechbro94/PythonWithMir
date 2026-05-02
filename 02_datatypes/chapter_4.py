is_boiling = True
stri_count = 5
total_actions = stri_count + is_boiling # upcasting
print(f"Total actions: {total_actions}")

milk_present = 0 # no milk
print(f"Is there milk? {bool(milk_present)}")

water_hot = True
coffee_added = True

can_serve = water_hot and coffee_added
print(f"Can serve coffee? {can_serve}")