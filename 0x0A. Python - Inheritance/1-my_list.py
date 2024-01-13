#!/usr/bin/python3
"""This class represents a list class"""


class MyList(list):
    """
    Customized list class, derived off the built-in list class.

    Methods:
        print_sorted(): Print the elements of the list in sorted order.

    Attributes:
        Inherits all attributes off the built-in list class.

    Usage Example:
        my_list = MyList([3, 1, 4, 1, 5, 9, 2])
        my_list.print_sorted()  # Output: [1, 1, 2, 3, 4, 5, 9]
    """
    def print_sorted(self):
        """
        Print the elements of the list in sorted order.

        Returns:
            list: The sorted list.
        """
        return sorted(self, reverse=False)
