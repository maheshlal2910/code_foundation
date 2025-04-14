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


class Line:
    def __init__(self, beginning: tuple, end: tuple):
        self.x1, self.y1 = beginning
        self.x2, self.y2 = end
    
    def length(self):
        return ((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5
    
    def slope(self):
        if self.x2 - self.x1 == 0:
            return float('inf')
        return (self.y2 - self.y1) / (self.x2 - self.x1)


def distance_between(point1: Point, point2: Point) -> float:
    if point1 == point2:
        return 0
    return ((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2) ** 0.5


def parallel_lines(line1: Line, line2: Line) -> bool:
    return math.isclose(line1.slope(), line2.slope())


def perpendicular_lines(line1: Line, line2: Line) -> bool:
    if abs(line1.slope()) == float('inf') and line2.slope() == 0:  # line1 is vertical, line2 is horizontal
        return True
    if abs(line2.slope()) == float('inf') and line1.slope() == 0:  # line2 is vertical, line1 is horizontal
        return True
    if abs(line1.slope()) != float('inf') and abs(line2.slope()) != float('inf'):
        return math.isclose(line1.slope() * line2.slope(), -1)


def intersects(line1: Line, line2: Line) -> bool:
    return not (parallel_lines(line1, line2))
