#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(int(value)))
    except TypeError as e:
        print(e)
