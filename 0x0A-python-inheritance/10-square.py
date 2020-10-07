#!/usr/bin/python3
"""Square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """vars initialization"""

        self.__size = size
        super().integer_validator("size", size)
        super().__init__(size, size)
