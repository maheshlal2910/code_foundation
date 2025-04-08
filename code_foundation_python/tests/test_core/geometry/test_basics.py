import unittest
from code_foundation.core.geometry.basics import Line


class TestLine(unittest.TestCase):

    def test_line_length(self):
        line = Line((1, 2), (4, 6))
        length = line.length()
        self.assertAlmostEqual(length, 5.0)

    def test_should_return_slope_of_line(self):
        line1 = Line((0, 0), (5, 5))
        self.assertEqual(line1.slope(), 1.0)

    def test_slope_is_undefined(self):
        line = Line((1, 1), (1, 1))
        self.assertEqual(line.slope(), float('inf'))
