import unittest
from shape_area import Circle, Triangle


class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(2)
        self.assertAlmostEqual(circle.area(), 12.566, places=3)

    def test_invalid_circle(self):
        circle = Circle(-5)
        self.assertFalse(circle.is_valid())

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.area(), 6)

    def test_invalid_triangle(self):
        triangle = Triangle(1, 2, 5)
        self.assertFalse(triangle.is_valid())

    def test_right_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_triangle())

    def test_not_right_triangle(self):
        triangle = Triangle(3, 3, 3)
        self.assertFalse(triangle.is_right_triangle())
        
if __name__ == "__main__":
    unittest.main()