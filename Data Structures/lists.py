letters = ["a", "b", "c"]

matrix = [[0, 1], [2, 3]]

zeros = [0] * 5

combined = zeros + letters

numbers = list(range(20))

chars = list("Hello Wrld")

print(chars)
print(len(chars))

# Accessing Items
letters[0] = "A"
print(letters[0])
print(letters[-1])
print(letters[0:3])
print(letters[::2])   # Every second element
print(letters[::-1])   # Every element in reverse order

# List Unpacking
numbers = [1, 2, 3]
# first = numbers[0]
# second = numbers[1]
# third = numbers[2]
first, second, third = numbers

numbers = [1, 2, 3, 4, 5, 6, 7]
first, second, *others = numbers

numbers = [1, 2, 3, 4, 5, 6, 7]
first,  *others, second = numbers

# Looping over Lists
letters = ["a", "b", "c"]
for index, letter in enumerate(letters):
    print(index, letter)

# Adding or Removing Items
# Add
letters = ["a", "b", "c"]
letters.append("d")
letters.insert(0, "-")

# Remove
letters.pop()
letters.pop(0)
letters.remove("b")
del letters[0:3]
letters.clear()
print(letters)

# Finding Items
letters = ["a", "b", "c"]
print(letters.count("d"))
if "d" in letters:
    print(letters.index("d"))

# Sorting Lists
numbers = [3, 51, 2, 8, 6]
numbers.sort()
numbers.sort(reverse=True)
sorted(numbers)
sorted(numbers, reverse=True)

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product1", 12),
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)
