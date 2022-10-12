#!/usr/bin/python3

"""
Module 6-square
Introduces getters and setters
"""


class Square:
    """
    Introduces getters and setters to obtain Area of square
    """

    def __init__(self, size=0, position=(0, 0)):
        """Instance initialization"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter for position field
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for position field
        """
        if not isinstance(
            value, tuple) or len(value) != 2 or type(
            value[0]) is not int or type(
                value[1]) is not int or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Computes Area of Square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints square in #'s using position
        """
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join([" " * self.__position[0] + "#" *
                  self.__size for rows in range(self.__size)]))
