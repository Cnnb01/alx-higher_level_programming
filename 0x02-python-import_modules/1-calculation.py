#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    a = 10
    b = 5
    sum1 = add(a, b)
    subt = sub(a, b)
    mult = mul(a, b)
    divi = div(a, b)
    print("{} + {} = {}".format(a, b, sum1))
    print("{} - {} = {}".format(a, b, subt))
    print("{} * {} = {}".format(a, b, mult))
    print("{} / {} = {}".format(a, b, divi))
