class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
p = Point()
p2 = Point(2, 3) 
print(p,p2)