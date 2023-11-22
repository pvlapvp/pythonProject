import math


class Dot:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.color = None

    def __str__(self):
        return f"x = {self.x}, y = {self.y}, color = {self.color}"

    def set_color(self, color = 'white'):
        self.color = color

class Circle(Dot):
    def __init__(self, x, y, r=1):
        super().__init__(x, y)
        self.r = r

    def __str__(self):
        return f"x = {self.x}, y = {self.y}, r = {self.r}, color = {self.color}"

    def area(self):
        return math.pi * self.r ** 2

    def set_radius(self, r):
        self.r = r

class Sphere(Circle):
    def __init__(self, x, y, r):
        super().__init__(x, y, r)

    def volume(self):
        return (4 * math.pi * (self.r ** 3))/3

    def area(self):
        pass

c = Circle(1, 2, 3)
print(c.area())
s = Sphere(1, 1, 3)
print(s.area())
print(s.volume())