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
