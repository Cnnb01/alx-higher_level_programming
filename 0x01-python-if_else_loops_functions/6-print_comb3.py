#!/usr/bin/python3
for i in range(0, 10):
    for t in range(i+1, 10):
        if i != t:
            print("{}{}".format(i, t), end=", " if i != 8 or t != 9 else "\n")
