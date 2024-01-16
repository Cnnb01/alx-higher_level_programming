#!/usr/bin/python3
"""
Adds all command line arguments to a Python list and saves it to a file.

Usage:
    ./script_name.py arg1 arg2 ...

The script reads command line arguments and adds them to a list. It then uses
the 'save_to_json_file' function to save the list as a JSON representation in
a file named 'add_items_to_list.json'.
If the file doesn't exist, it is created.

Functions:
    add_items_to_list: Adds command line arguments to a Python list.

Modules:
    sys: Provides access to some variables
    used or maintained by the Python interpreter
    save_to_json_file: Custom function to save a Python object as a JSON file
    load_from_json_file: Custom function to load a Python
    object from a JSON file
"""

import sys


def add_items_to_list():

    """
    Adds command line arguments to a Python list.

    Returns:
        list: A list containing the command line arguments.
    """
    my_list = []
    for i in sys.argv[1:]:
        my_list.append(i)
    return my_list


if __name__ == "__main__":

    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__(
        '6-load_from_json_file').load_from_json_file

    my_list = add_items_to_list()
    save_to_json_file(my_list, "add_items_to_list.json")
