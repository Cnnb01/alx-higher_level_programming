#!/usr/bin/python3
"""
Converts a JSON-formatted string to a Python object.

Usage:
    result = from_json_string(my_str)

The function takes a JSON-formatted string and returns the
corresponding Python object.

Parameters:
    my_str (str): The JSON-formatted string to be converted.

Returns:
    obj: The Python object obtained from parsing the JSON string.

Modules:
    json: Provides methods for working with JSON data.
    io: Provides tools for working with I/O operations.
"""

import json
from io import StringIO


def from_json_string(my_str):
    """
    Converts a JSON-formatted string to a Python object.

    Args:
        my_str (str): The JSON-formatted string to be converted.

    Returns:
        obj: The corresponding Python object.
    """
    io = StringIO(my_str)
    return json.loads(io.getvalue())
