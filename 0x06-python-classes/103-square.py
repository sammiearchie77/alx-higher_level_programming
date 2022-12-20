#!/usr/bin/python3
import math

class MagicClass:
    """set up the magic"""
    def __init__(self, radius):
        """ Constructor """
        self.__radius = 0
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """ Find the area """

        return self.__radius ** 2 * math.pi

    def circumference(self):
        """ get circumference """

        return 2 * math.pi * self.__radius

