#!/usr/bin/python3

"""
Module 3-square

Computes the area of a square
"""


class Square:
    """
    A class that computes the area of a square
    """

    def __init__(self, size=0):
        """
        Checks if size is an integer and is >= 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculates the area of the square
        """
        return self.__size * self.__size
