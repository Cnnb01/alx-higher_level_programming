#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_set = []
    for i in my_list:
        if i not in new_set:
            new_set.append(i)
    summation = sum(i for i in new_set)
    return (summation)
