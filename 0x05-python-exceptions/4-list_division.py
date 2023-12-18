#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    quot = []
    try:
        if len(my_list_1) < list_length or len(my_list_2) < list_length:
            print("out of range")
            return quot
        for i, j in zip(my_list_1[:list_length], my_list_2[:list_length]):
            try:
                result = i/j
                quot.append(result)
            except ZeroDivisionError:
                print("division by 0")
                quot.append(0)
    except TypeError:
        print("wrong type")
        quot.append(0)
    finally:
        return quot
