#!/usr/bin/python3
for i in range(0, 99):
    if i < 10:
        print("{} = 0x{}".format(i, i % 10))
    elif i == 10:
        print("{} = 0x{}".format(i, chr(97)))
    elif i == 11:
        print("{} = 0x{}".format(i, chr(98)))
    elif i == 12:
        print("{} = 0x{}".format(i, chr(99)))
    elif i == 13:
        print("{} = 0x{}".format(i, chr(100)))
    elif i == 14:
        print("{} = 0x{}".format(i, chr(101)))
    elif i == 15:
        print("{} = 0x{}".format(i, chr(102)))
    else:
        print("{} = {}".format(i, hex(i)))
