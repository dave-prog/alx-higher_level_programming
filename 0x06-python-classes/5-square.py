#!/usr/bin/python3

"""
Module 4-square
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

    def my_print(self):
        """
        Prints the square in form of #
        """
        print("\n".join(["#" * self.__size for rows in range(self.__size)]))
