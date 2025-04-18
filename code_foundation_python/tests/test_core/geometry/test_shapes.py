import math
import unittest

from code_foundation.core.geometry.line import Line, perpendicular_lines
from code_foundation.core.geometry.point import Point
from code_foundation.core.geometry.shapes import Quadrilateral, Rectangle, Square


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
    
    def test_unequal_opposite_side_lengths_raise_an_error(self):
        """Test that a rectangle with unequal opposite sides raises an error."""
        with self.assertRaises(ValueError):
            Rectangle(
                Point(0, 0),
                Point(0, 2),
                Point(4, 2),  # Side length 4 (opposite side is invalid)
                Point(3, 0)
            )
    
    def test_non_right_angles_raises_an_error(self):
        """Test that a rectangle with angles that are not right angles raises an error."""
        with self.assertRaises(ValueError):
            Rectangle(
                Point(0, 0),
                Point(0, 2),
                Point(2, 3),  # Non-perpendicular angle
                Point(3, 0)
            )
    
    def test_rectangle_unique_vertices(self):
        """Test that a rectangle must have exactly 4 unique vertices."""
        with self.assertRaises(ValueError):
            Rectangle(
                Point(0, 0),
                Point(0, 3),
                Point(5, 3),
                Point(0, 0)  # Duplicate vertex
            )
    
    def test_rectangle_perimeter(self):
        """Test that the parameter() method calculates the perimeter correctly."""
        rect = Rectangle(
            Point(0, 0),
            Point(0, 4),
            Point(6, 4),
            Point(6, 0)
        )
        self.assertEqual(
            rect.perimeter(),
            20,
            "The calculated perimeter of the rectangle is incorrect."
        )


class TestSquareValidation(unittest.TestCase):
    
    def test_valid_square(self):
        try:
            square = Square(
                Point(0, 0),
                Point(0, 4),
                Point(4, 4),
                Point(4, 0)
            )
            
            # Ensure it is a valid quadrilateral
            self.assertEqual(
                len(set(square.vertices)),
                4,
                "Square vertices are not distinct (not a valid quadrilateral)."
            )
            
            # Assert that all vertices are stored correctly
            self.assertEqual(
                square.vertices,
                [Point(0, 0), Point(0, 4), Point(4, 4), Point(4, 0)],
                "Vertices are not stored correctly for a valid square."
            )
            
            # Ensure all sides are equal
            self.assertTrue(
                all(
                    math.isclose(square.sides[0].length(), side.length())
                    for side in square.sides
                ),
                "Not all sides of the square are equal."
            )
            
            # Verify adjacent sides are perpendicular
            for i in range(4):
                self.assertTrue(
                    perpendicular_lines(square.sides[i], square.sides[(i + 1) % 4]),
                    "Adjacent sides do not form right angles for a valid square."
                )
        except Exception as e:
            self.fail(f"Valid square creation failed: {e}")
    
    def test_square_with_duplicate_vertices(self):
        """Test that a square with duplicate vertices raises an error."""
        with self.assertRaises(ValueError):
            Square(
                Point(0, 0),
                Point(0, 4),
                Point(4, 4),
                Point(0, 0)  # Duplicate vertex
            )
    
    def test_square_perimeter(self):
        """Test that the square's perimeter calculation respects the quadrilateral behavior."""
        square = Square(
            Point(0, 0),
            Point(0, 3),
            Point(3, 3),
            Point(3, 0)
        )
        self.assertEqual(
            square.perimeter(),
            12,
            "The calculated perimeter of the square is incorrect."
        )
    
    def test_square_invalid_sides(self):
        """Test that a square with unequal adjacent sides raises an error."""
        with self.assertRaises(ValueError):
            Square(
                Point(0, 0),
                Point(0, 4),
                Point(6, 4),  # Opposite sides equal
                Point(6, 0)  # Adjacent sides are unequal
            )
    
    def test_square_invalid_angles(self):
        """Test that a square with non-right angles raises an error."""
        with self.assertRaises(ValueError):
            Square(
                Point(0, 0),
                Point(0, 3),
                Point(2, 4),  # Invalid angle
                Point(3, 0)
            )
    
    