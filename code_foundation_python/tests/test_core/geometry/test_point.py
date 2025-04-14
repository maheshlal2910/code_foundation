import unittest
import math

from code_foundation.core.geometry.point import Point, distance_between


class TestPoint(unittest.TestCase):
    def test_points_with_same_cooridinates_are_equal(self):
        point1 = Point(1, 2)
        point2 = Point(1, 2)
        self.assertEqual(point1, point2)
    
    def test_points_with_different_cooridinates_are_not_equal(self):
        point1 = Point(1, 2)
        point3 = Point(2, 3)
        self.assertNotEqual(point1, point3)
    
    def test_points_with_same_cooridinates_but_different_types_are_equal(self):
        point1 = Point(1, 2)
        point4 = Point(1, 2.0)
        self.assertEqual(point1, point4)
    
    def test_point_and_non_point_are_not_equal(self):
        point1 = Point(1, 2)
        not_a_point = (1, 2)
        self.assertNotEqual(point1, not_a_point)
    
    def test_point_and_none_are_not_equal(self):
        point1 = Point(1, 2)
        self.assertNotEqual(point1, None)


class TestPointDistance(unittest.TestCase):
    def test_distance_between_positive_and_negative_coordinates(self):
        point1 = Point(3, 4)
        point2 = Point(-6, -8)
        distance = distance_between(point1, point2)
        expected_distance = math.sqrt((3 - -6) ** 2 + (4 - -8) ** 2)
        self.assertAlmostEqual(distance, expected_distance)
    
    def test_distance_between_identical_points_is_zero(self):
        point1 = Point(2, 3)
        point2 = Point(2, 3)
        self.assertAlmostEqual(distance_between(point1, point2), 0.0)
    
    def test_distance_between_two_points_with_horizontal_difference(self):
        point1 = Point(1, 5)
        point2 = Point(4, 5)
        distance = distance_between(point1, point2)
        expected_distance = abs(4 - 1)
        self.assertAlmostEqual(distance, expected_distance)
