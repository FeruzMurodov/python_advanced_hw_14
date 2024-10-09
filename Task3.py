class Rectangle:
    """
    >>> r1 = Rectangle(5,6)
    >>> r1.get_dimensions()
    '(5, 6)'
    >>> r1.set_dimensions(6,7)
    >>> r1.get_dimensions()
    '(6, 7)'
    >>> r1.get_area()
    42
    >>> r1.get_perimeter()
    26
    >>> r1.set_dimensions(-1,-2)
    Traceback (most recent call last):
    ...
    ValueError: Sides have to be positive
    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def set_dimensions(self, width, height):
        if width > 0 and height > 0:
            self.__width = width
            self.__height = height
        else:
            raise ValueError('Sides have to be positive')

    def get_area(self):
        return self.__width * self.__height

    def get_perimeter(self):
        return (self.__width + self.__height) * 2

    def get_dimensions(self):
        return f'{self.__width, self.__height}'


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
