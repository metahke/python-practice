class Shape:
    def calc_area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def calc_area(self):
        return 4 * self.length
