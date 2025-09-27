from .base import Shape

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        if not self._is_valid_triangle(side1, side2, side3):
            raise ValueError("Invalid triangle sides")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def area(self):
        s = self.perimeter() / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3
    
    def _is_valid_triangle(self, a, b, c):
        return (a + b > c) and (a + c > b) and (b + c > a) and (a > 0) and (b > 0) and (c > 0)
    
    def is_right_triangle(self, tolerance=1e-7):
        sides = sorted([self.side1, self.side2, self.side3])
        return abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < tolerance
