import unittest
from Unit_tests.rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_area_negative(self):
        self.assertEqual(area(-5, 5), -25) 

    def test_perimeter(self):
        self.assertEqual(perimeter(10, 5), 30)
if __name__ == '__main__':
    unittest.main()