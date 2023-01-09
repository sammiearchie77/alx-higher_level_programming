#!/usr/bin/python3

""" A class MyList that inherits from list """

class MyList(list):
    def print_sorted(self):
        """ prints a sorted list """
        printed(self.sort())
