from data import *
import lab4
import unittest


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


    # Part 5


    # Part 6





if __name__ == '__main__':
    unittest.main()
