items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product1", 12),
]

# prices = [expression for item in items]

prices = [item[1] for item in items]  # Map alternative

filtered = [item for item in items if item[1] >= 10]  # Filter alternative
