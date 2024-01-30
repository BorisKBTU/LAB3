class Shape:
    def __init__(self):
        self.area_ = 0

    def area(self):
        print(self.area_)


class Square(Shape):
    def __init__(self, a):
        self.length = a
        self.area_square = 0

    def area(self):
        self.area_square = self.length ** 2
        print(self.area_square)


sq = Square(5)
sq.area()
sh = Shape()
sh.area()
