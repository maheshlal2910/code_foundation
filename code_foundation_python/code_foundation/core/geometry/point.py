import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return math.isclose(self.x, other.x) and math.isclose(self.y, other.y)
        return False
    
    def __hash__(self):
        return hash((round(self.x, 10), round(self.y, 10)))


def distance_between(point1: Point, point2: Point) -> float:
    if point1 == point2:
        return 0
    return ((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2) ** 0.5

