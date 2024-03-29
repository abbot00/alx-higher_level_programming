#!/usr/bin/python3
"""  a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)

Private instance attribute: width:
property def width(self): to retrieve it
property setter def width(self, value): to set it:
width must be an integer, otherwise raise a TypeError
exception with the message width must be an integer
if width is less than 0, raise a ValueError exception with the
message width must be >= 0
Private instance attribute: height:
property def height(self): to retrieve it
property setter def height(self, value): to set it:
height must be an integer, otherwise raise a TypeError
exception with the message height must be an integer
if height is less than 0, raise a ValueError exception
with the message height must be >= 0
Instantiation with optional width and height:
def __init__(self, width=0, height=0):"""


class Rectangle:
    """an empty class tha defines a rectangle"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter of the property width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of the property width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter of the property height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of the property height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calclulates the area of a rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """" Calculates the perimeter of a rectangle"""
        if (self.width == 0 or self.height == 0):
            return 0
        return (self.__width * 2 + self.__height*2)
