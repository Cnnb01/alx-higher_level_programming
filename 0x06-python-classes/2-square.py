#!/usr/bin/python3
"""This class represents a square"""


class Square:
    """This class represents a square with height and width attributes."""
    def __init__(self, size=0):
        """
    Initialize the square with the given size.
    Args:
    size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
