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
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """
    Get the size of the square.
    Returns:
    int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
    Set the size of the square.
    Args:
    value (int): The value to set as the size.
    Raises:
    TypeError: If the size is not an integer.
    ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
    Calculate the area of the square.
    Returns:
    int: The area of the square.
        """
        return int(self.__size) * int(self.__size)
