#!/usr/bin/python3
"""Rectangle class with private width"""


class Rectangle:
    """Rectangle class with private width"""

    number_of_instances = 0

    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """vars initialization"""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ("")
        xvar = ""
        for i in range(self.height):
            xvar += str(self.print_symbol) * self.width
            xvar += "\n"
        return (xvar[:-1])

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def width(self, value):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value