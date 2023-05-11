class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return f"Point({self.x}, {self.y})"
class Polygon:
    def __init__(self):
        self.points = []

    def add_point(self, point):
        if isinstance(point, Point):
            self.points.append(point)
        else:
            raise TypeError("Można dodawać tylko instancje klasy Point do klasy Polygon")

    def __str__(self):
        points_str = ', '.join(str(p) for p in self.points)
        return f"Polygon[{points_str}]"
p1 = Point(2, 3)
p2 = Point(1, 1)
p3 = Point(4, 2)

polygon = Polygon()
polygon.add_point(p1)
polygon.add_point(p2)
polygon.add_point(p3)

print(polygon)
