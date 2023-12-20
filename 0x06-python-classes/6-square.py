#!/usr/bin/python3
"""This class represents a square"""


class Square:
    """This class represents a square with height and width attributes."""
    def __init__(self, size=0, position=(0, 0)):
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
        self.__position = position

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

    @property
    def position(self):
        """
    Get the position of the square.
    Returns:
    tuple: The position of the square.
        """
        return self.__size

    @position.setter
    def position(self, value):
        """
    Set the position of the square.
    Args:
    value (tuple): The value to set as the position.
    Raises:
    TypeError: If the position is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple):
            if len(value) == 2:
                raise TypeError("position must be a tuple of 2 +tive integers")
            self.__size = value

    def area(self):
        """
        Calculate the area of the square.
        Returns:
        int: The area of the square.
        """
        return int(self.__size) * int(self.__size)

    def my_print(self):
        """
        Print a square made out of "#" characters.
        """
        if self.__size == 0:
            print()
        else:
            for k in range(self.__position[0]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[1], end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
