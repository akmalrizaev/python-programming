from sys import getsizeof

values = (x * 2 for x in range(10))
print(values)
for x in values:
    print(x)

values = (x * 2 for x in range(100000))
print("gen:", getsizeof(values))      # gen: 120

values = [x * 2 for x in range(100000)]
print("list:", getsizeof(values))      # list: 824464
