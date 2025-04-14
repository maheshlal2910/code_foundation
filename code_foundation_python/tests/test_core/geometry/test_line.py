import unittest


from code_foundation.core.geometry.point import Point
from code_foundation.core.geometry.line import Line, parallel_lines, perpendicular_lines, \
    intersects


class TestLine(unittest.TestCase):
    
    def test_line_length(self):
        line = Line(Point(1, 2), Point(4, 6))
        length = line.length()
        self.assertAlmostEqual(length, 5.0)
    
    def test_should_return_slope_of_line(self):
        line1 = Line(Point(0, 0), Point(5, 5))
        self.assertEqual(line1.slope(), 1.0)


class TestParallelLines(unittest.TestCase):
    
    def test_parallel_lines(self):
        line1 = Line(Point(0, 0), Point(1, 1))
        line2 = Line(Point(2, 2), Point(3, 3))
        self.assertTrue(parallel_lines(line1, line2))
    
    def test_not_parallel_lines(self):
        line1 = Line(Point(0, 0), Point(1, 2))
        line2 = Line(Point(0, 0), Point(2, 1))
        self.assertFalse(parallel_lines(line1, line2))


class TestPerpendicularLines(unittest.TestCase):
    
    def test_perpendicular_lines_which_are_not_vertical_or_horizontal(self):
        line1 = Line(Point(1, 1), Point(3, 3))
        line2 = Line(Point(2, 0), Point(0, 2))
        self.assertTrue(perpendicular_lines(line1, line2))
    
    def test_non_perpendicular_lines(self):
        line1 = Line(Point(0, 0), Point(2, 1))
        line2 = Line(Point(1, 1), Point(3, 3))
        self.assertFalse(perpendicular_lines(line1, line2))
    
    def test_vertical_and_horizontal_lines_perpendicular(self):
        line1 = Line(Point(0, 0), Point(0, 5))  # Vertical line
        line2 = Line(Point(0, 0), Point(5, 0))  # Horizontal line
        self.assertTrue(perpendicular_lines(line1, line2))
    
    def test_horizontal_and_vertical_lines_are_perpendicular(self):
        line1 = Line(Point(0, 0), Point(5, 0))
        line2 = Line(Point(0, 0), Point(0, 5))
        self.assertTrue(perpendicular_lines(line1, line2))


class TestLineIntersection(unittest.TestCase):
    
    def test_vertical_and_diagonal_lines_intersect(self):
        line1 = Line(Point(1, 0), Point(1, 5))
        line2 = Line(Point(0, 1), Point(2, 3))
        self.assertTrue(intersects(line1, line2))
    
    def test_horizontal_and_diagonal_lines_intersect(self):
        line1 = Line(Point(0, 1), Point(0, 5))
        line2 = Line(Point(0, 1), Point(2, 3))
        self.assertTrue(intersects(line1, line2))
    
    def test_perpendicular_lines_should_intersect(self):
        line1 = Line(Point(1, 1), Point(3, 3))
        line2 = Line(Point(2, 0), Point(0, 2))
        self.assertTrue(intersects(line1, line2))
    
    def test_parallel_lines_should_not_intersect(self):
        line1 = Line(Point(0, 0), Point(1, 1))
        line2 = Line(Point(2, 2), Point(3, 3))
        self.assertFalse(intersects(line1, line2))
