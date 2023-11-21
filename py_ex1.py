class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"width = {self.width} - length = {self.length}"

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return self.width + self.length

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area() == other.area()
        else: return False

s = Rectangle(2, 3)
t = Rectangle(3, 4)

print(s)
print(t)

print(s.area())
print(s.perimeter())
print(s.__eq__(t))