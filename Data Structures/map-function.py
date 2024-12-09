items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product1", 12),
]

prices = []
for item in items:
    prices.append(item[1])

print(prices)

# Map Function
prices = list(map(lambda item: item[1], items))
print(prices)
