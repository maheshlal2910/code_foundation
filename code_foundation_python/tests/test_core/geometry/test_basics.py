import unittest
from code_foundation.core.geometry.basics import Line

class TestLine(unittest.TestCase):
    def test_line_length(self):
        line = Line((1, 2), (4, 6))
        length = line.length()
        self.assertAlmostEqual(length, 5.0)