from code_foundation.core.geometry.point import Point

class Quadrilateral:
    def __init__(self, v1:Point, v2: Point, v3: Point, v4: Point):
        if len({v1, v2, v3, v4}) != 4:
            raise ValueError("All vertices of the quadrilateral must be distinct.")
        
        self.vertices = [v1, v2, v3, v4]
