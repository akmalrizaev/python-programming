try:
    age = int(input("Age: "))
except ValueError:
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
print("Execution continues.")


try:
    age = int(input("Age: "))
except ValueError as ex:
    print("You didn't enter a valid age.")
    print(ex)
    print(type(ex))
else:
    print("No exceptions were thrown.")
print("Execution continues.")


try:
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")


try:
    file = open("app.py")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
finally:
    file.close()
