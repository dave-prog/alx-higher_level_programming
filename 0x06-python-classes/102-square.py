#!/usr/bin/python3

"""
Module 102-square
Introduces getters and setters
"""


class Square:
    """
    Introduces getters and setters to obtain Area of square
    """

    def __init__(self, size=0):
        """Instance initialization"""
        self.size = size

    @property
    def size(self):
        """Initializes getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Checks the if size is of integer type and is >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Computes Area of Square
        """
        return self.__size * self.__size

    def __eq__(self, other):
        """ Checks equality between objects """
        return self.size == other.size

    def __ne__(self, other):
        """ Checks if objects are no equal """
        return self.size != other.size

    def __gt__(self, other):
        """ Checks if size is greater than other """
        return self.size > other.size

    def __ge__(self, other):
        """ Checks if size is greater than or equal to other """
        return self.size >= other.size

    def __lt__(self, other):
        """ Checks if size is lesser than or greatr than other """
        return self.size < other.size

    def __le__(self, other):
        """ Checks if size is lesser than or equal to other """
        return self.size <= other.size
