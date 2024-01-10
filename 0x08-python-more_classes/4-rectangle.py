#!/usr/bin/python3
"""This module defines the Rectangle class."""


class Rectangle:
    """This class represents a rectangle with height and width attributes."""

    def __init__(self, width=0, height=0):
        """Initialize a rectangle with a given width and height.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The new width value.

        Raises:
            ValueError: If the width is less than 0.
            TypeError: If the width is not an integer.
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
        """Set the height of the rectangle.

        Args:
            value (int): The new height value.

        Raises:
            ValueError: If the height is less than 0.
            TypeError: If the height is not an integer.
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Generate a string representation of the rectangle using '#' symbols.

        Returns:
            str: A string representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        count = ""
        for i in range(self.__height):
            for j in range(self.__width):
                count += "#"
            count += "\n"
        return count

    def __repr__(self):
        """Generate a string representation of the rectangle for debugging.

        Returns:
            str: A string representation of the rectangle object.
        """
        return f"Rectangle({self.__width}, {self.__height})"
