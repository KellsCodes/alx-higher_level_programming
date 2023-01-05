#!/usr/bin/python3

"""
The matrix division module
The module contains matrix_divide function
that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    matrix_divide function

    args:
        matrix: list of lists of integers or floats
        div: number type of integer or float and not equal to 0

    Returns:
        a new matrix, all elements of the matrix are divided by div
        rounded to 2 decimal places
    """
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        type_msg = ("matrix must be a matrix (list of lists) of "
                    "integers/floats")

        if (not matrix or type(matrix) is not list or len(matrix) < 1 or
                type(matrix[0]) is not list):
            raise TypeError(type_msg)
        new_matrix = []
        matrix_len = 0

        for matrix_list in matrix:
            if type(matrix_list) is not list:
                raise TypeError(type_msg)
            if matrix_len != 0 and len(matrix_list) != matrix_len:
                raise TypeError(
                    "Each row of the matrix must have the same size")
            new_list = []
            matrix_len = len(matrix_list)
            for value in matrix_list:
                if not type(value) in (int, float):
                    raise TypeError(type_msg)
                new_list.append(round((value / div), 2))
            new_matrix.append(new_list)
        return new_matrix
