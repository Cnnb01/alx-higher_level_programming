# 0x0B. Python - Input/Output

## Overview

In programming, Input/Output (I/O) refers to the processes of providing information to a program (input) and receiving results or messages from the program (output). In Python, I/O operations are crucial for interacting with users, reading and writing files, and handling data.

This README provides a brief overview of key concepts and practices related to Python Input/Output.

## Input

### Reading User Input

Python offers the `input()` function to receive user input. It prompts the user for input and returns the entered value as a string.

Example:
```python
user_input = input("Enter something: ")
print("You entered:", user_input)
```

### Command-Line Arguments

Python scripts can accept command-line arguments using the `sys.argv` list or the `argparse` module. This allows passing values to a script when it is executed from the command line.

Example (using sys.argv):
```python
import sys

script_name = sys.argv[0]
argument1 = sys.argv[1]
argument2 = sys.argv[2]

print("Script name:", script_name)
print("Argument 1:", argument1)
print("Argument 2:", argument2)
```

## Output

### Printing to the Console

The `print()` function is fundamental for displaying output to the console. It can take multiple arguments and concatenate them for display.

Example:
```python
name = "John"
age = 25
print("Name:", name, "Age:", age)
```

### Writing to Files

Python provides methods for reading and writing files. The `open()` function is used to open a file, and the `read()` and `write()` methods are used for reading from and writing to files.

Example (writing to a file):
```python
with open("output.txt", "w") as file:
    file.write("Hello, World!")
```

## Exception Handling

Exception handling is crucial for dealing with potential errors during I/O operations. Using `try`, `except`, and `finally` blocks helps handle errors gracefully.

Example:
```python
try:
    file = open("nonexistent.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    file.close()
```