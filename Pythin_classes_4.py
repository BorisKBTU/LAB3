from math import sqrt


class Point:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def show(self):
        print(self.coordinates)

    def dist(self, another_point):
        return sqrt(sum([(i[0] - i[1]) ** 2 for i in zip(self.coordinates, another_point)]))

    def move(self, new_coordinates):
        self.coordinates = new_coordinates


point = Point((0, 0))
point.show()
print(point.dist((5, 6)))
point.move((2, 2))
point.show()
print(point.dist((5, 6)))
