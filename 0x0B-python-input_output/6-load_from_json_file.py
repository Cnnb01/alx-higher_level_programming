#!/usr/bin/python3
"""
Loads a Python object from a JSON file.

Usage:
    loaded_object = load_from_json_file("filename.json")

The function reads the content of a JSON file and converts
it into a Python object.
It returns the loaded object.

Functions:
    load_from_json_file: Loads a Python object from a JSON file.

Modules:
    json: Provides methods for working with JSON data.
"""

import json


def load_from_json_file(filename):
    """
    Loads a Python object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        obj: The Python object loaded from the JSON file.
    """
    with open(filename, encoding="utf-8") as f:
        data = f.read()
        return json.loads(data)
