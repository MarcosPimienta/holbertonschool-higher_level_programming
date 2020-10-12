#!/usr/bin/python3
""" Rectangle class """


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
            return ("[Square] ({}) {}/{} - {})"
                    .format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        attrs = ["id", "size", "x", "y"]
        argslen = len(args)
        if args is not None and argslen is not 0:
            for i in range(argslen):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
