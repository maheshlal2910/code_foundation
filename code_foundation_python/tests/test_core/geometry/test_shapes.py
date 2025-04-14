import unittest
import math

from code_foundation.core.geometry.point import Point
from code_foundation.core.geometry.line import Line, perpendicular_lines
from code_foundation.core.geometry.shapes import Quadrilateral, Rectangle


class TestQuadrilateral(unittest.TestCase):
    
    def test_quadrilateral_with_non_distinct_vertices(self):
        with self.assertRaises(ValueError):  # Assuming ValueError is raised for invalid quadrilaterals
            Quadrilateral(Point(0, 0), Point(1, 1), Point(0, 0), Point(2, 2))
    
    def test_quadrilateral_with_distinct_vertices(self):
        try:
            Quadrilateral(Point(0, 0), Point(1, 1), Point(2, 2), Point(3, 3))
        except Exception as e:
            self.fail(f"Quadrilateral creation failed with distinct vertices: {e}")
    
    def test_quadrilateral_perimeter(self):
        quad = Quadrilateral(Point(0, 0), Point(0, 1), Point(1, 1), Point(1, 0))
        perimeter = quad.perimeter()
        self.assertEqual(perimeter, 4, "Perimeter calculation is incorrect")


class TestRectangleValidation(unittest.TestCase):
    
    def test_rectangle_valid(self):
        """Test that a rectangle with valid vertices is created successfully."""
        try:
            rect = Rectangle(
                Point(0, 0),
                Point(0, 3),
                Point(5, 3),
                Point(5, 0)
            )
            self.assertEqual(
                rect.vertices,
                [Point(0, 0), Point(0, 3), Point(5, 3), Point(5, 0)],
                "Vertices are not stored correctly for a valid rectangle."
            )
            
            lines = [
                Line(rect.vertices[i], rect.vertices[(i + 1) % 4])
                for i in range(4)
            ]
            
            self.assertTrue(
                math.isclose(lines[0].length(), lines[2].length()),
                "Opposite sides are not equal in length for a valid rectangle."
            )
            self.assertTrue(
                math.isclose(lines[1].length(), lines[3].length()),
                "Opposite sides are not equal in length for a valid rectangle."
            )
            
            for i in range(4):
                self.assertTrue(
                    perpendicular_lines(lines[i], lines[(i + 1) % 4]),
                    "Adjacent sides do not form right angles for a valid rectangle."
                )
        except Exception as e:
            self.fail(f"Valid rectangle creation failed: {e}")
    
    def test_rectangle_with_invalid_side_lengths(self):
        """Test that a rectangle with unequal opposite sides raises an error."""
        with self.assertRaises(ValueError):
            Rectangle(
                Point(0, 0),
                Point(0, 2),
                Point(4, 2),  # Side length 4 (opposite side is invalid)
                Point(3, 0)
            )
    
    def test_rectangle_with_non_right_angles(self):
        """Test that a rectangle with angles that are not right angles raises an error."""
        with self.assertRaises(ValueError):
            Rectangle(
                Point(0, 0),
                Point(0, 2),
                Point(2, 3),  # Non-perpendicular angle
                Point(3, 0)
            )
