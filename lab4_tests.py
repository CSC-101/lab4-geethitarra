from data import *
import lab4
import unittest
import math
# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_first_element_1(self):
        input = [[1,2], [3,4]]
        result = lab4.first_element(input)
        expected = [1, 3]
        self.assertEqual(expected, result)

    def test_first_element_2(self):
        input = [[], [3, 4]]
        result = lab4.first_element(input)
        expected = [3]
        self.assertEqual(expected, result)

    # Part 2
    def test_x_coordinates(self):
        point1 = Point(4.0, 3.0)
        point2 = Point(-3.0, 8)
        point3 = Point(0, 0)
        point4 = Point(0, 3)
        point_list = [point1, point2, point3, point4]
        result = lab4.x_coordinates(point_list)
        expected = [4.0, -3.0, 0, 0]
        self.assertEqual(expected, result)

    def test_x_coordinates2(self):
        point1 = Point(100.0, 0)
        point2 = Point(0, 80)
        point3 = Point(-10, -9)
        point_list = [point1, point2, point3]
        result = lab4.x_coordinates(point_list)
        expected = [100.0, 0, -10]
        self.assertEqual(expected, result)

    # Part 3
    def test_are_in_positive_quadrant(self):
        point1 = Point(4.0, 3.0)
        point2 = Point(-3.0, 8)
        point3 = Point(0, 0)
        point4 = Point(0, 3)
        point_list = [point1, point2, point3, point4]
        result = lab4.are_in_positive_quadrant(point_list)
        expected = [point1, point3, point4]
        self.assertEqual(expected, result)

    def test_are_in_positive_quadrant2(self):
        point1 = Point(-4.0, -3.0)
        point2 = Point(-3.0, 8)
        point3 = Point(0, 0)
        point4 = Point(0, 3)
        point_list = [point1, point2, point3, point4]
        result = lab4.are_in_positive_quadrant(point_list)
        expected = [point3, point4]
        self.assertEqual(expected, result)

    # Part 4
    def test_distance(self):
        point1 = Point(3.0, 4.0)
        point2 = Point (0, 0)
        result = lab4.distance(point1, point2)
        expected = 5.65
        self.assertAlmostEqual(expected, result, 1)

    def test_distance2(self):
        point1 = Point(0, 0)
        point2 = Point(1, 0)
        result = lab4.distance(point1, point2)
        expected = 1
        self.assertAlmostEqual(expected, result, 1)

    # Part 5
    def manhattan_distance(self):
        point1 = Point(0, 0)
        point2 = Point(1, 0)
        result = lab4.manhattan_distance(point1, point2)
        expected = 1
        self.assertAlmostEqual(expected, result, 1)

    def manhattan_distance2(self):
        point1 = Point(4, 0)
        point2 = Point(18, 0)
        result = lab4.manhattan_distance(point1, point2)
        expected = 14
        self.assertAlmostEqual(expected, result, 1)


    # Part 6
    def distance_all(self):
        point1 = Point(1.0, 0.0)
        point2 = Point(0, 0)
        point_list = [point1, point2]
        result = lab4.distance_all()
        expected = 1
        self.assertAlmostEqual(expected, result, 1)

    def distance_all2(self):
        point1 = Point(8.0, 0.0)
        point2 = Point(10, 0)
        point_list = [point1, point2]
        result = lab4.distance_all()
        expected = 8, 10
        self.assertAlmostEqual(expected, result, 1)




if __name__ == '__main__':
    unittest.main()
