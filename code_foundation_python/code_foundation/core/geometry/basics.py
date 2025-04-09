import math


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