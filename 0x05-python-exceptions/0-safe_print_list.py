#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in my_list:
            if count < x:
                print(i, end="")
                count = count + 1
            else:
                break
        print()
        return count
    except IndexError as e:
        print(e)
