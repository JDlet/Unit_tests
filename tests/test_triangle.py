import unittest
from geometric_lib.triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(area(0, 10), 0)

    def test_area_positive(self):
        self.assertEqual(area(10, 5), 25.0)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0, 0, 0), 0)

    def test_perimeter_positive(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
if __name__ == '__main__':
    unittest.main()