#!/usr/bin/python3

"""child class Square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class representing a square, which is a special case of a rectangle.

    Attributes:
        size (int): The size of the square (both width and height are equal).
        x (int): The x-coordinate of the square.
        y (int): The y-coordinate of the square.
        id (int): The identifier for the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square (both width and height).
            x (int): The x-coordinate of the square.
            y (int): The y-coordinate of the square.
            id (int): The identifier for the square. If None,
            a new ID will be generated.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """int: The size of the square (both width and height)."""
        return self.width

    @size.setter
    def size(self, new_width):
        """
        Set the size of the square.

        Args:
            new_width (int): The new size value.

        Raises:
            TypeError: If new_width is not an integer.
            ValueError: If new_width is less than or equal to 0.
        """
        self.width = new_width
        self.height = new_width

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: String representation of the square.
        """
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """
        Update the attributes of the square with the provided arguments.

        Args:
            *args: List of positional arguments.
            **kwargs: Dictionary of keyword arguments.
        """
        if len(args):
            for i, a in enumerate(args):
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.size = a
                elif i == 2:
                    self.x = a
                elif i == 3:
                    self.y = a
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        Return a dictionary representation of the square.

        Returns:
            dict: Dictionary representation of the square.
        """
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
