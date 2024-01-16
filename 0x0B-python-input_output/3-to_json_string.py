#!/usr/bin/python3
"""
Converts a Python object to a JSON-formatted string.

Usage:
    json_str = to_json_string(my_obj)

The function takes a Python object and returns its
JSON-formatted string representation.

Parameters:
    my_obj: The Python object to be converted to a JSON string.

Returns:
    str: The JSON-formatted string representation of the input object.

Modules:
    json: Provides methods for working with JSON data.
    io: Provides tools for working with I/O operations.
"""

import json
from io import StringIO


def to_json_string(my_obj):
    """
    Converts a Python object to a JSON-formatted string.

    Args:
        my_obj: The Python object to be converted.

    Returns:
        str: The JSON-formatted string representation of the input object.
    """
    io = StringIO()
    json.dump(my_obj, io)
    return io.getvalue()
