#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    x = (sorted(a_dictionary.keys()))
    for i in x:
        val = a_dictionary[i]
        print(f"{i}: {val}")
