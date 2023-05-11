class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def __mul__(self, n):
        return Point(self.x * n, self.y * n)
p1 = Point(2, 3)
p2 = p1 * 2

print(p1) 
print(p2)
