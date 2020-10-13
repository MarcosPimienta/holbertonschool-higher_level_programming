#!/usr/bin/python3
""" Rectangle class """


from models.base import Base


class Rectangle(Base):
    """Class rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def area(self):
        """Class rectangle area"""
        return (self.__width * self.__height)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """Class rectangle height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def width(self, value):
        """Class rectangle width"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def width(self):
        """Class rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Class rectangle width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def y(self):
        """Class rectangle y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Class rectangle y setter"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def x(self, value):
        """Class rectangle x setter"""
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def x(self):
        """Class rectangle x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Class rectangle x setter"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    def display(self):
        """Class rectangle display"""
        print("\n" * self.__y + (' ' * self.__x + "#" * self.width + "\n") *
              self.height, end="")

    def __str__(self):
        """Class rectangle print"""
        return ("[Rectangle] ({}) {}/{} - {}/{})"
                .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """Class rectangle update"""
        attrs = ["id", "width", "height", "x", "y"]
        argslen = len(args)
        if args is True:
            for i in range(argslen):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Class rectangle to dictionary"""
        dic2 = {"x": self.x,
                "y": self.y,
                "id": self.id,
                "height": self.height,
                "width": self.width}
        return (dic2)
