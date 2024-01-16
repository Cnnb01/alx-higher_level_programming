#!/usr/bin/python3
"""
Writes text to a file and prints the character count.

Usage:
    write_file(filename, text)

The function writes the specified text to the given
file and prints the total character count in the file.

Parameters:
    filename (str): The name of the file to which the text will be written.
    text (str): The text to be written to the file.

Modules:
    None

Raises:
    None

Example:
    write_file("example.txt", "This is a sample text.")
"""


def write_file(filename="", text=""):
    """
    Writes text to a file and prints the character count.

    Args:
        filename (str): The name of the file.
        text (str): The text to write.

    Raises:
        None
    """
    with open(filename, mode='w', encoding="utf-8") as f:
        f.write(text)

    with open(filename, encoding="utf-8") as f:
        charcount = 0
        for line in f:
            for char in line:
                charcount += 1
    return charcount
