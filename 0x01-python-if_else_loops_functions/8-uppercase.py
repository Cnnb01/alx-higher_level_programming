#!/usr/bin/python3
def uppercase(str):
    up_str = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            up_str = up_str + chr(ord(i) - 32)
        else:
            up_str = up_str + i
    print("{}{}".format(up_str))
