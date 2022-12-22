#!/usr/bin/python3
""" class Square that defines a square"""


class Square:
    """class square that defines a square"""

    def __init__(self, size=0):
        """initialize size of square
        Args:
            size(init): size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size  # size of the square

    def area(self):
        """Returns the area of a number"""
        return self.__size**2
