from shape import Shape

class Rectangle(Shape):

    def __init__(self, color, length, width):
        super().__init__(color)
        self._length = length
        self._width = width

    @property
    def length(self):
        return self._length

    @length.setter
    def radius(self, length):
        self._length = length

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    def area(self):
        return self._length * self._width