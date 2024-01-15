#!/usr/bin/python3
"""
Definition of the "Square" class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Square initialization"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """fecthes size"""
        return self.width

    @size.setter
    def size(self, value):
        """sets size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Representation of informal string of the square"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                         self.y, self.width)

    def update(self, *args, **kwargs):
        """Attributes update"""
        if len(args):
            for m, n in enumerate(args):
                if m == 0:
                    self.id = n
                elif m == 1:
                    self.size = n
                elif m == 2:
                    self.x = n
                elif m == 3:
                    self.y = n
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """dictionary representation of a Square"""
        dic = {}
        dic["id"] = self.id
        dic["size"] = self.size
        dic["x"] = self.x
        dic["y"] = self.y
        return dic
