class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, offsetx, offsety):
        self.x += offsetx
        self.y += offsety

    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

p = Point()
print(p)
p.move(5, -8)
print(p)