class Rectangle:
    """
    Прямоугольник с возможностью сравнения по площади
    """

    def __init__(self, width, length):
        self.a = length * width

    def area(self):
        return self.a

    def __eq__(self, other):
        if other.a:
            return self.a == other.a

    def __ne__(self, other):
        if other.a:
            return self.a != other.area

    def __lt__(self, other):
        if other.a:
            return self.a < other.a

    def __gt__(self, other):
        if other.a:
            return self.a > other.a


r1 = Rectangle(3, 5)
r2 = Rectangle(4, 5)

print("{} == {} = {}".format(r1.area(), r2.area(), r1 == r2))
print("{} != {} = {}".format(r1.area(), r2.area(), r1 != r2))
print("{} < {} = {}".format(r1.area(), r2.area(), r1 < r2))
print("{} > {} = {}".format(r1.area(), r2.area(), r1 > r2))
