class Animal():
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


# Animal: Parent, Base
# Mammal: Child, Sub
class Mammal(Animal):
    def __init__(self):
        super().__init__()
        self.weight = 2

    def walk(self):
        print("walk")


class Fish(Animal):

    def swim(self):
        print("swim")


m = Mammal()
m.eat()


print(isinstance(m, Mammal))  # True
print(isinstance(m, Animal))  # True
print(isinstance(m, object))  # True

o = object()

print(issubclass(Mammal, Animal))  # True
print(issubclass(Mammal, object))  # True
