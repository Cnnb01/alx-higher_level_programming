#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    Check if an object inherits from a specific class.

    Args:
        obj: The object to be checked.
        a_class: The class to check inheritance against.

    Returns:
        bool: True if the object inherits from the
        specified class; otherwise, False.
    """
    actual_class = type(obj)

    if issubclass(actual_class, a_class):
        return True

    return False
