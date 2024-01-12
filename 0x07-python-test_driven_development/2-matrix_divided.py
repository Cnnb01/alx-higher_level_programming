#!/usr/bin/python3
def matrix_divided(matrix, div):
    for i in matrix:
        if isinstance(matrix[i], (int, float)):
            if isinstance(div, (int, float)):
                if div == 0:
                    raise ZeroDivisionError("division by zero")
                return matrix[i] / div
            raise TypeError("div must be a number")
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")