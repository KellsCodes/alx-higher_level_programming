#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """class Square with private instance attribute"""

    def __init__(self, size=0):
        """
        Initializing the class instance
        Args: size(int) size of square
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of square, private member
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of square, must be an integer"""
        if type(value) is not int:
            raise TypeError("size must be an interger")
        elif value < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the area of the square"""
        return self.__size**2
