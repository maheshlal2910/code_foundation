import math

from code_foundation.core.geometry.point import Point, distance_between


class Line:
    def __init__(self, beginning: Point, end: Point):
        self.beginning = beginning
        self.end = end
    
    def length(self):
        return distance_between(self.beginning, self.end)
    
    def slope(self):
        if self.end.x - self.beginning.x == 0:
            return float('inf')
        return (self.end.y - self.beginning.y) / (self.end.x - self.beginning.x)


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
