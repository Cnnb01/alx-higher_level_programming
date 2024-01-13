#!/usr/bin/python3
"""Returns a list of all available attributes and methods"""


def lookup(obj):
    """
    Returns a list of callable attributes/methods of the given object.

    Args:
        obj: Any Python object.

    Returns:
        list: A list containing the names of callable attributes/methods.
    """
    return dir(obj)
