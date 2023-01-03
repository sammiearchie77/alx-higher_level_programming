#!/usr/bin//python3

""" Defines a Rectangle Class """

class Rectangle:
    """ A Class of Rectangle with a width and height attribute. """

    def __init__(self, width=0, height=0):
         """Initializes a Rectangle instance.
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self._width = width
        self._height = height

    def __str__(self):
        """ Returns an informal and nicely printable string representation
        of a Rectangle instance, filled with the '#' character. """
        if self._height == 0 or self._width == 0:
            return ''
        rec_str = ''
        for i in range(self._height):
            for j in range(self._width):
                rec_str += '#'
            rec_str += '\n'
        return rec_str[:-1]

    @property
    def width(self):
        """ Retrieve the width of a Rectangle instance """
        return self._width

    @width.setter
    def width(self, value):
        """Sets the width of a Rectangle instance
        Args:
            value: value of the width, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of a Rectangle instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a Rectangle instance
        Args:
            value: value of the height, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of a Rectangle instance
        Returns:
            Area of the the rectangle, given by height * width
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of a Rectangle instance
        Returns:
            Perimeter of the rectangle, given by 2 * (height + width)
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
