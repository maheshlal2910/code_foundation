import unittest

from code_foundation.core.geometry.point import Point
from code_foundation.core.geometry.shapes import Quadrilateral


class TestQuadrilateral(unittest.TestCase):
    
    def test_quadrilateral_with_non_distinct_vertices(self):
        with self.assertRaises(ValueError):  # Assuming ValueError is raised for invalid quadrilaterals
            Quadrilateral(Point(0, 0), Point(1, 1), Point(0, 0), Point(2, 2))

    def test_quadrilateral_with_distinct_vertices(self):
        try:
            Quadrilateral(Point(0, 0), Point(1, 1), Point(2, 2), Point(3, 3))
        except Exception as e:
            self.fail(f"Quadrilateral creation failed with distinct vertices: {e}")
    