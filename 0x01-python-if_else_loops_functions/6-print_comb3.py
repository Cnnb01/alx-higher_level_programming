#!/usr/bin/python3
for i in range(0, 10):
    for items in range(i+1, 10):
        if i != items:
            print(f"{i}{items}", end=", ")
        else:
            continue
