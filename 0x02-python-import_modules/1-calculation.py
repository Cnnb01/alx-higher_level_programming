#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    a = 10
    b = 5
    sum1 = add(a, b)
    subt = sub(a, b)
    mult = mul(a, b)
    divi = div(a, b)
    print(f"{a} + {b} = {sum1}")
    print(f"{a} - {b} = {subt}")
    print(f"{a} * {b} = {mult}")
    print(f"{a} / {b} = {divi}")
