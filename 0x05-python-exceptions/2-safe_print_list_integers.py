#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in my_list:
            if isinstance(i, int) and count < x:
                print("{:d}".format(i), end="")
                count = count + 1
        print()
        return count
    except (IndexError, TypeError) as e:
         print(e)
