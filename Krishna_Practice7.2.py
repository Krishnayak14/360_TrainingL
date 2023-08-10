# 2. Define a class named Shape and its subclass Square. The Square class has an init function which takes length as argument.
# Both classes have an area function which can print the area of the shape where Shape’s area is 0 by default.


class Shape:
    def area(self):
        return 0

class Square(Shape):
    x = 0
    y = 0
    def __init__(self, length):
        self.x = length
        self.y = length
    def area(self):
        return self.x * self.y

sq = Square(10)

print(sq.area())
