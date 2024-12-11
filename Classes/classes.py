class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point.zero()
Point.default_color = "yellow"
point = Point(1, 2)
print(type(point))
print(isinstance(point, Point))
print(point.default_color)
print(Point.default_color)

print(point.x)
point.draw()

another = Point(3, 4)
print(another.default_color)
another.draw()
