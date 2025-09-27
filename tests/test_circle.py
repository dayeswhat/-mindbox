import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from shapes import Circle
import math

class TestCircle(unittest.TestCase):
    
    def test_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), math.pi * 25)
    
    def test_perimeter(self):
        circle = Circle(3)
        self.assertAlmostEqual(circle.perimeter(), 2 * math.pi * 3)
    
    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            Circle(-1)
    
    def test_zero_radius(self):
        with self.assertRaises(ValueError):
            Circle(0)

if __name__ == '__main__':
    unittest.main()
