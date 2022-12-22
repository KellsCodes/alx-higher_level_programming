#!/usr/bin/python3
"""class Square"""


class Square:
    """class Sqaure for printing square"""

    def __init__(self, size=0):
        """Initializes instance size attribute, must be an int"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """Retrieves the size of the square"""
        return self.__size

    @size.setter
    def size(self, size):
        """Resets the value of size attribute, must be an integer"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    
    def area(self):
        """Returns the current area of the square"""
        return self.__size**2
    
    def my_print(self):
        """prints the square in stdout with the character #"""
        if self.__size == 0:
            print()
        else:
            for vertical in range(0, self.__size):
                for horizontal in range(0, self.__size):
                    print("#", end="")
                print()


