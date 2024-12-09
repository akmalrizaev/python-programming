items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product1", 12),
]

filtered = list(filter(lambda item: item[1] >= 10, items))

print(filtered)
