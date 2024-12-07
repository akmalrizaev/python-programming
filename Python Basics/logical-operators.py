name = "  "
if not name.strip():
    print("Name is Empty")

age = 22
if 18 <= age < 65:
    print("Eligible")

# ------------------------------

age = 22
if age >= 18:
    message = "Eligible"
else:
    message = "Not eligible"

# Ternary Operator
message = "Eligible" if age >= 18 else "Not eligible"
