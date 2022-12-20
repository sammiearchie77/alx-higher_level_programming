#!/usr/bin/python3

class Square:
    """ Square class """
    def __init__(self, size=0):
        """__init__ method that sets the size of square.
        Args:
            size (int): size of Square
        Raises:
            TypeError: If `size` is not an integer.
            ValueError: If `size` is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an intege")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Get the area of the square.
        Returns:
            Area of square
        """
        return self.__size * self.__size
