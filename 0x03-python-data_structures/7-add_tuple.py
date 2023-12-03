#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = len(tuple_a)
    b = len(tuple_b) 
    if a < 2:
        tuple_a = tuple_a + (0,) * (2-a)
    if b < 2:
        tuple_b = tuple_b + (0,) * (2-b)                        
    elif len(tuple_a) > 2 or len(tuple_b) > 2:
        return((tuple_a[:2], tuple_b[:2]))
    else:
        sum1 = tuple_a[0] + tuple_b[0]
        sum2 = tuple_a[1] + tuple_b[1]
        return(sum1, sum2)
