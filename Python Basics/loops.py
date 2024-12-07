for x in "Python":
    print(x)

for x in ['a', 'b', 'c']:
    print(x)

for x in range(2, 5):
    print(x)

# For..Else

names = ["AJohn", "Mary"]
for name in names:
    if name.startswith("J"):
        print("Found")
        break
else:
    print("Not found")

# While Loops

guess = 0
answer = 5

while answer != guess:
    guess = int(input("Guess: "))
