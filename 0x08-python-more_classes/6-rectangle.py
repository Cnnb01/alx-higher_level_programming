#!/usr/bin/python3
"""This module defines the Rectangle class."""


class Rectangle:
    """Class representing a rectangle."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The width value to set.
        Raises:
            ValueError: If width is less than 0.
            TypeError: If width is not an integer.
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The height value to set.
        Raises:
            ValueError: If height is less than 0.
            TypeError: If height is not an integer.
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        count = ""
        for i in range(self.__height):
            for j in range(self.__width):
                count += "#"
            count += "\n"
        return count

    def __repr__(self):
        """
        Return a string representation of the rectangle for debugging.

        Returns:
            str: The string representation of the rectangle.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Destructor method to print a farewell message
        when a rectangle instance is deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
