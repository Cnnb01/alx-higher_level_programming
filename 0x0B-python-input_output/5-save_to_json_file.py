#!/usr/bin/python3
"""
Saves a Python object to a JSON file.

Usage:
    save_to_json_file(my_obj, "filename.json")

The function takes a Python object and writes it to a JSON file.

Functions:
    save_to_json_file: Saves a Python object to a JSON file.

Modules:
    json: Provides methods for working with JSON data.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Saves a Python object to a JSON file.

    Args:
        my_obj: The Python object to be saved.
        filename (str): The name of the JSON file to save.

    Returns:
        None
    """
    with open(filename, mode='w', encoding="utf-8") as f:
        json.dump(my_obj, f)
