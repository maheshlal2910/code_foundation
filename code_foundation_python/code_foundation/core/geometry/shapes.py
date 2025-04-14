from code_foundation.core.geometry.point import Point, distance_between


class Quadrilateral:
    def __init__(self, v1: Point, v2: Point, v3: Point, v4: Point):
        if len({v1, v2, v3, v4}) != 4:
            raise ValueError("All vertices of the quadrilateral must be distinct.")
        
        self.vertices = [v1, v2, v3, v4]
    
    def perimeter(self):
        return sum(
            distance_between(self.vertices[i], self.vertices[(i + 1) % 4])
            for i in range(4)
        )


from code_foundation.core.geometry.point import Point
from code_foundation.core.geometry.line import Line, perpendicular_lines
from code_foundation.core.geometry.shapes import Quadrilateral
import math


class Rectangle(Quadrilateral):
    def __init__(self, v1: Point, v2: Point, v3: Point, v4: Point):
        # Initialize the parent Quadrilateral class for basic validation
        super().__init__(v1, v2, v3, v4)
        
        # Create lines representing the sides of the rectangle
        self.sides = [
            Line(self.vertices[i], self.vertices[(i + 1) % 4])
            for i in range(4)
        ]
        
        # Validate that opposite sides are equal in length
        if not (
                math.isclose(self.sides[0].length(), self.sides[2].length())
                and math.isclose(self.sides[1].length(), self.sides[3].length())
        ):
            raise ValueError("Opposite sides of the rectangle must have equal lengths.")
        
        # Validate that all adjacent sides are perpendicular
        for i in range(4):
            if not perpendicular_lines(self.sides[i], self.sides[(i + 1) % 4]):
                raise ValueError("All adjacent sides must form right angles.")
