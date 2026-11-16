import unittest
import math
from geometric_lib.circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_positive(self):
        self.assertAlmostEqual(area(2), math.pi * 4)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_positive(self):
        self.assertAlmostEqual(perimeter(3), 2 * math.pi * 3)

if __name__ == '__main__':
    unittest.main()