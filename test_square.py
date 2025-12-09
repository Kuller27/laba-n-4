import unittest
import square

class SquareTestCase(unittest.TestCase):
    def test_area_zero_side(self):
        res = square.area(0)
        self.assertEqual(res, 0)
    
    def test_area_positive_integer(self):
        res = square.area(5)
        self.assertEqual(res, 25)
    
    def test_area_positive_float(self):
        res = square.area(2.5)
        self.assertEqual(res, 6.25)
    
    def test_perimeter_zero_side(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)
    
    def test_perimeter_positive_integer(self):
        res = square.perimeter(5)
        self.assertEqual(res, 20)
