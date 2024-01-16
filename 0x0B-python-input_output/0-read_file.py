#!/usr/bin/python3
"""
Reads and prints the contents of a file.

Usage:
    read_file(filename)

The function reads the contents of the specified
file and prints them to the console.

Parameters:
    filename (str): The name of the file to be read.

Modules:
    None

Raises:
    None

Example:
    read_file("example.txt")
"""


def read_file(filename=""):
    """
    Reads and prints the contents of a file.

    Args:
        filename (str): The name of the file.

    Raises:
        None
    """
    with open(filename, encoding="utf-8") as f:
        content = f.read()
        print(content)
