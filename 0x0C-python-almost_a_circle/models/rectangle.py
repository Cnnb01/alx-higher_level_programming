#!/usr/bin/python3

"""Child class Rectangle"""

from models.base import Base


class Rectangle(Base):
    """
    Class representing a rectangle.

    Attributes:
        id (int): The identifier for the rectangle.
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
        __x (int): The x-coordinate of the rectangle.
        __y (int): The y-coordinate of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle.
            y (int): The y-coordinate of the rectangle.
            id (int): The identifier for the rectangle.
            If None, a new ID will be generated.
        """
        Base.__init__(self, id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, val):
        """
        Set the width of the rectangle.

        Args:
            val (int): The new width value.

        Raises:
            TypeError: If val is not an integer.
            ValueError: If val is less than or equal to 0.
        """
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        elif val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, val):
        """
        Set the height of the rectangle.

        Args:
            val (int): The new height value.

        Raises:
            TypeError: If val is not an integer.
            ValueError: If val is less than or equal to 0.
        """
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        elif val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @property
    def x(self):
        """int: The x-coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, val):
        """
        Set the x-coordinate of the rectangle.

        Args:
            val (int): The new x-coordinate value.

        Raises:
            TypeError: If val is not an integer.
            ValueError: If val is less than 0.
        """
        if not isinstance(val, int):
            raise TypeError("x must be an integer")
        elif val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        """int: The y-coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, val):
        """
        Set the y-coordinate of the rectangle.

        Args:
            val (int): The new y-coordinate value.

        Raises:
            TypeError: If val is not an integer.
            ValueError: If val is less than 0.
        """
        if not isinstance(val, int):
            raise TypeError("y must be an integer")
        elif val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        """Calculate the area of the rectangle."""
        return self.__height * self.__width

    def display(self):
        """
        Display the rectangle by printing '#' characters to the console.
        """
        count = ""
        for _ in range(self.__y):
            count += "\n"
        for i in range(self.__height):
            count += " " * self.__x
            count += "#" * self.__width
            count += "\n"
        print(count)

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            str: String representation of the rectangle.
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.__x, self.__y,
                        self.__width, self.__height))

    def update(self, *args, **kwargs):
        """
        Update the attributes of the rectangle with the provided arguments.

        Args:
            *args: List of positional arguments.
            **kwargs: Dictionary of keyword arguments.
        """
        up = ["id", "width", "height", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, up[i], args[i])
        else:
            for k in kwargs:
                setattr(self, k, kwargs[k])

    def to_dictionary(self):
        """
        Return a dictionary representation of the rectangle.

        Returns values
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
