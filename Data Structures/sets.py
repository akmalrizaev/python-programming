numbers = [1, 1, 2, 3, 4]
uniques = set(numbers)
print(uniques)
second = {1, 4}
second.add(5)
second.remove(5)
len(second)

numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 5}

print(first | second)  # Set Union

print(first & second)  # Set Intersection

print(first - second)  # Difference Sets

print(first ^ second)  # Semantic difference

if 1 in first:
    print("yes")
