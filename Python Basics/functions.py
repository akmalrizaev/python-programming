def increment(number, by=1):
    return (number, number + by)


print(increment(5, 3))


def decrement(number: int, by: int = 1) -> tuple:
    return (number, number + by)


print(decrement(5))
