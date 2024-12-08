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
