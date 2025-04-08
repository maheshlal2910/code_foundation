import unittest

from code_foundation.core.geometry.basics import Line, parallel_lines, perpendicular_lines


class TestLine(unittest.TestCase):

    def test_line_length(self):
        line = Line((1, 2), (4, 6))
        length = line.length()
        self.assertAlmostEqual(length, 5.0)

    def test_should_return_slope_of_line(self):
        line1 = Line((0, 0), (5, 5))
        self.assertEqual(line1.slope(), 1.0)


class TestLineFunctions(unittest.TestCase):

    def test_parallel_lines(self):
        line1 = Line((0, 0), (1, 1))
        line2 = Line((2, 2), (3, 3))
        self.assertTrue(parallel_lines(line1, line2))

    def test_vertical_and_horizontal_lines_perpendicular(self):
        line1 = Line((0, 0), (0, 5))  # Vertical line
        line2 = Line((0, 0), (5, 0))  # Horizontal line
        self.assertTrue(perpendicular_lines(line1, line2))

    def test_not_parallel_lines(self):
        line1 = Line((0, 0), (1, 2))
        line2 = Line((0, 0), (2, 1))
        self.assertFalse(parallel_lines(line1, line2))

    def test_perpendicular_lines(self):
        line1 = Line((1, 1), (3, 3))
        line2 = Line((2, 0), (0, 2))
        self.assertTrue(perpendicular_lines(line1, line2))

    def test_non_perpendicular_lines(self):
        line1 = Line((0, 0), (2, 1))
        line2 = Line((1, 1), (3, 3))
        self.assertFalse(perpendicular_lines(line1, line2))

    def test_horizontal_and_vertical_lines_are_perpendicular(self):
        line1 = Line((0, 0), (5, 0))  # Horizontal line
        line2 = Line((0, 0), (0, 5))  # Vertical line
        self.assertTrue(perpendicular_lines(line1, line2))
