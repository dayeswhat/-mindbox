import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from shapes import Triangle

class TestTriangle(unittest.TestCase):
    
    def test_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0)
    
    def test_perimeter(self):
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.perimeter(), 12)
    
    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            Triangle(1, 1, 3)
    
    def test_is_right_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_triangle())
        
        triangle2 = Triangle(3, 3, 3)
        self.assertFalse(triangle2.is_right_triangle())

if __name__ == '__main__':
    unittest.main()
