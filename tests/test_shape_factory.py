import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from shapes import ShapeFactory

class TestShapeFactory(unittest.TestCase):
    
    def test_create_circle(self):
        circle = ShapeFactory.create_shape("circle", 5)
        self.assertEqual(circle.radius, 5)
    
    def test_create_triangle(self):
        triangle = ShapeFactory.create_shape("triangle", 3, 4, 5)
        self.assertEqual(triangle.side1, 3)
        self.assertEqual(triangle.side2, 4)
        self.assertEqual(triangle.side3, 5)
    
    def test_invalid_shape_type(self):
        with self.assertRaises(ValueError):
            ShapeFactory.create_shape("square", 5)

if __name__ == '__main__':
    unittest.main()
