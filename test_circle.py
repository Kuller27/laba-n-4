import unittest
import math
import circle

class CircleTestCase(unittest.TestCase):
    def test_area_zero_radius(self):
        res = circle.area(0)
        self.assertEqual(res, 0)
    
    def test_area_positive_integer(self):
        res = circle.area(5)
        expected = math.pi * 25
        self.assertEqual(res, expected)
    
    def test_area_positive_float(self):
        res = circle.area(2.5)
        expected = math.pi * 6.25
        self.assertAlmostEqual(res, expected, places=7)
    
    def test_perimeter_zero_radius(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)
    
    def test_perimeter_positive_integer(self):
        res = circle.perimeter(5)
        expected = 2 * math.pi * 5
        self.assertEqual(res, expected)
