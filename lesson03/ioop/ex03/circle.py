from shape import Shape
import math

class Circle(Shape):

    def __init__(self, color, radius):
        super().__init__(color)
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        self._radius = radius

    def area(self):
        return math.pi * self._radius**2