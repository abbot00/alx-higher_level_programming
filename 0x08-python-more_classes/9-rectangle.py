#!/usr/bin/python3
"""  a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)

"""


class Rectangle:
    """an empty class tha defines a rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """method that prints a rectangle with #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = [str(self.print_symbol) * self.__width for
                character in range(self.__height)]
        return '\n'.join(rect)

    def __repr__(self):
        """Returns an “official” string representation of a Rectangle"""
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        """ prints to stdout when a rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """a method that returns the bigger triangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """class method to create a square Rectangle"""
        return cls(size, size)
