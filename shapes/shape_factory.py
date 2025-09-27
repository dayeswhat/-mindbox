from .circle import Circle
from .triangle import Triangle
from .rectangle import Rectangle

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type, *args):
        shape_type = shape_type.lower()
        
        if shape_type == "circle" and len(args) == 1:
            return Circle(args[0])
        elif shape_type == "triangle" and len(args) == 3:
            return Triangle(*args)
        elif shape_type == "rectangle" and len(args) == 2:
            return Rectangle(*args)
        else:
            raise ValueError(f"Unsupported shape type or invalid arguments: {shape_type}")
