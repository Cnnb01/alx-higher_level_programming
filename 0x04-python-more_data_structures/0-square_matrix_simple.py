#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squares = []
    for i in matrix:
        squared_i = [j ** 2 for j in i]
        squares.append(squared_i)
    return (squares)
