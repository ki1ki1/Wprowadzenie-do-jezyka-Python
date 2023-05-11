class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def __mul__(self, n):
        return Point(self.x * n, self.y * n)
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False
p1 = Point(2, 3)
p2 = Point(2, 3)
p3 = Point(4, 6)

print(p1 == p2) 
print(p1 == p3) 
