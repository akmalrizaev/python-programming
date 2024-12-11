class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


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
