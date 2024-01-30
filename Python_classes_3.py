class Shape:
    def __init__(self):
        pass

    def area(self):
        if isinstance(self, Square):
            print(self.length ** 2)
        elif isinstance(self, Rectangle):
            print(self.length * self.width)
        else:
            print(0)


class Square(Shape):
    def __init__(self, a):
        self.length = a


class Rectangle(Shape):
    def __init__(self, a, b):
        self.length = a
        self.width = b


sq = Square(5)
sq.area()
sh = Shape()
sh.area()
rec = Rectangle(9, 6)
rec.area()
