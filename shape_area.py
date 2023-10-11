from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def is_valid(self):
        pass
    
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * (self.radius ** 2)
    
    def is_valid(self):
        return self.radius > 0
    
    
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def area(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
    
    def is_valid(self):
         return self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a
     
    def is_right_triangle(self):
        a, b, c = sorted([self.a, self.b, self.c])
        return a**2 + b**2 == c**2