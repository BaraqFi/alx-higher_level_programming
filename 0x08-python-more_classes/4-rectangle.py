#!/usr/bin/python3


"""Represents a reactangle"""


class Rectangle:
    """Define Rectangle"""
    def __init__(self, width=0, height=0):
        """initialize a new rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the width of rectangle"""
        return (self.__width)

    @property
    def height(self):
        return (self.__height)

    @width.setter
    def width(self, value):
        """sets a new width value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """sets a new height value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            P = 0
            return P
        P = 2 * (self.width + self.height)
        return P

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ("")

        rect = []
        for i in range(self.height):
            [rect.append('#') for j in range(self.width)]
            if i != self.height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        rect = "Rectangle(" + str(self.width)
        rect += ", " + str(self.height) + ")"
        return (rect)
