point = (1, 2)
point = (1, 2) + (3, 4)  # (1,2,3,4)
point(1, 2) * 3  # (1,2,1,2,1,2)
point = tuple([1, 2])  # convert to tuple
point = tuple("Hello World")
point = (1, 2, 3)
print(point[0:2])

if 10 in point:
    print("exists")

print(point)
