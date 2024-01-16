#!/usr/bin/python3
"""
Appends text to a file and prints the character count.

Usage:
    append_write(filename, text)

The function appends the specified text to the given
file and prints the total character count in the file.

Parameters:
    filename (str): The name of the file to which the text will be appended.
    text (str): The text to be appended to the file.

Modules:
    None

Raises:
    None

Note:
    The function does not handle file permission exceptions.

Example:
    append_write("example.txt", "This is a new line.")
"""


def append_write(filename="", text=""):
    """
    Appends text to a file and prints the character count.

    Args:
        filename (str): The name of the file.
        text (str): The text to append.
    """
    with open(filename, mode='a', encoding="utf-8") as f:
        f.write(text)

    with open(filename, encoding="utf-8") as f:
        charcount = 0
        for line in f:
            for char in line:
                charcount += 1
    return (charcount)
