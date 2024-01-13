#!/usr/bin/python3
"""The module is 3-is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or an instance
    of a subclass of a specific class.

    Args:
        obj: The object to be checked.
        a_class: The class to check against.

    Returns:
        bool: True if the object is an instance of the specified
        class or its subclass; otherwise, False.
    """
    if isinstance(obj, a_class):
        return True
    return False
