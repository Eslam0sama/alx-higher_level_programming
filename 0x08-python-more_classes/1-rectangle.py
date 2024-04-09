#!/usr/bin/python3
"""This is a module-level documentation string.

This is a module that provides a class of Rectangle and its methods.

"""


class Rectangle:
    """This is class-level documentation string.

This class represents a Rectangle object.
You can find more information about its attributes and methods below.

"""
    def __init__(self, width, height):
        """A function that initialize an Rectangle instance.

        Args:
            width (int): The width of the object
            height (int): The height of the object
        """

        self.__width = width
        self.__height = height

    @property
    def width(self, value):
        """A fucntion that retrieves the object width

        Args:
            value (int): Width's value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """A fucntion that set the value of object width

        Args:
            value (int): Width's value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self, value):
        """A fucntion that retrieves the object height

        Args:
            value (int): height's value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """A fucntion that set the value of object height

        Args:
            value (int): height's value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
