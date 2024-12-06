course = "Python Programming"
print(len(course))
print(course[0])
print(course[-1])
print(course[0:3])
print(course[:3])
print(course[0:])

print(id(course))
print(id(course[0]))

# Escape Sequence
message = "Python \"Programming"
print(message)

# Formatted Strings
first = "Akmal"
last = "Alex"
full = f"{first} {last}"
print(full)

# Useful String Methods
course = "  Python Programming"
print(course.upper())
print(course.lower())
print(course.title())

print(course.strip())

print(course.find("Pro"))
print(course.replace("P", "-"))

print("Programming" in course)
