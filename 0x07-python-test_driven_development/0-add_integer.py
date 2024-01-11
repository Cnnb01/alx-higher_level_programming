#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two numbers.

    The function takes two parameters, `a` and `b`, and returns their sum.

    Args:
        a (int or float): The first number.
        b (int or float): The second number. Defaults to 98.

    Returns:
        int: The sum of `a` and `b`.

    Raises:
        TypeError: If either `a` or `b` is not an integer or float.
    """
    if isinstance(a, (int, float)):
        if isinstance(a, float):
            int(a)
        if isinstance(b, (int, float)):
            if isinstance(b, float):
                int(b)
            return a + b
        raise TypeError("b must be an integer")
    raise TypeError("a must be an integer")