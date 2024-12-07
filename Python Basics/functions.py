def increment(number, by=1):
    return (number, number + by)


print(increment(5, 3))


def decrement(number: int, by: int = 1) -> tuple:
    return (number, number + by)


print(decrement(5))

# Arguments - *args


def multiply(*list):
    total = 1
    for number in list:
        total *= number
    return total


print(multiply(2, 3, 4, 5))

# Arguments- **args


def save_user(**user):
    print(user["name"])


save_user(id=1, name="admin")
