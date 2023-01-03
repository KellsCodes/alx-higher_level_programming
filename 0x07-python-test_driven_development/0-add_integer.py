#!/usr/bin/python3

"""
Python module for adding  two integer numbers
The function raises TypeError when a wrong data type is used
"""


def add_integer(a, b=98):
    """
    A function that adds two numbers of integer data type

    Args:
        a: first number
        b: second number

    Returns:
        the value of the added integers

    Raises:
        TypeError: if any of the args are not of integer or float types
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
