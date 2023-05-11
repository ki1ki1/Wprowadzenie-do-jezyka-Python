class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return f"Point({self.x}, {self.y})"
class Polygon:
    def __init__(self, points=None):
        self.points = [] if points is None else points
    
    def add_point(self, point):
        self.points.append(point)
    
    def __str__(self):
        return f"Polygon[{', '.join(str(p) for p in self.points)}]"
    
    def __getitem__(self, item):
        if isinstance(item, int):
            return self.points[item]
        elif isinstance(item, slice):
            return Polygon(self.points[item])
        else:
            raise TypeError("Nieprawidłowy typ argumentu")

p1 = Point(2, 3)
p2 = Point(1, 1)
p3 = Point(4, 2)

polygon = Polygon()
polygon.add_point(p1)
polygon.add_point(p2)
polygon.add_point(p3)


print(polygon[0])
print(polygon[1:])
