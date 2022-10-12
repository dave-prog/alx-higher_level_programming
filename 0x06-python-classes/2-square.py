#!/usr/bin/python3

"""
Module 2-square
"""


class Square:
    """ A class with private attribute 'size'"""

    def __init__(self, size=0):
        """ Private class of size
        Attributes: if size is not an integer output TypeError
        if size < 0 output ValueError
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
