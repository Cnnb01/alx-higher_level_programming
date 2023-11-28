#!/usr/bin/python3
for i in range(0, 10):
    for it in range(i+1, 10):
        if i != it:
            print("{}{}".format(i,it) , end=", " if i != 8 or it != 9 else "\n")
