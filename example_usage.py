import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from shapes import Circle, Triangle, Rectangle, ShapeFactory

def calculate_area_without_knowing_type(shape):
    return shape.area()

def main():
    shapes = [
        Circle(5),
        Triangle(3, 4, 5),
        Rectangle(4, 6),
        ShapeFactory.create_shape('circle', 3),
        ShapeFactory.create_shape('triangle', 5, 12, 13),
        ShapeFactory.create_shape('rectangle', 3, 7)
    ]
    
    print('Calculating areas without knowing shape type:')
    for i, shape in enumerate(shapes, 1):
        area = calculate_area_without_knowing_type(shape)
        print(f'{i}. {shape.__class__.__name__}: area = {area:.2f}')
    
    print('\nChecking right triangles:')
    triangles = [
        Triangle(3, 4, 5),
        Triangle(5, 12, 13),
        Triangle(3, 3, 3)
    ]
    
    for triangle in triangles:
        is_right = triangle.is_right_triangle()
        print(f'Triangle {triangle.side1}, {triangle.side2}, {triangle.side3}: {"right" if is_right else "not right"}')

if __name__ == '__main__':
    main()
