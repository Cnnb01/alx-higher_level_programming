#!/usr/bin/python3
"""The module is 2-is_same_class"""


def is_same_class(obj, a_class):
    """
    Check if an object is an instance of a specific class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        bool: True if the object is an instance of the
        specified class; otherwise, False.
    """
    return type(obj) is a_class
