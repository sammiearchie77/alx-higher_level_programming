#!/usr/bin/python3

""" Define a Rectangle Class """

class Rectangle:
    """ Rectangle class defined by width and height. """

    def __init__(self, width=0, height=0):
        """ Initializes a Rectangle instance.

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self._width = width
        self._height = height

    @property
    def width(self):
        """ Retrieve the width of the rectangle instance """
        return self._width

    @width.setter
    def width(self, value):
        """ Sets the width of a Rectangle instance

        Args:
            value: value of the width, must be a postive integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """ Retrieve the height of a Rectangle instance """
        return self._height

    @height.setter
    def height(self, value):
        """ Sets the height of a Rectangle instance

        Args:
            value: value of the height, must be an integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
