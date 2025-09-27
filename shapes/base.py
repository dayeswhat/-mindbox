from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    def __str__(self):
        return f'{self.__class__.__name__}: area={self.area():.2f}, perimeter={self.perimeter():.2f}'
