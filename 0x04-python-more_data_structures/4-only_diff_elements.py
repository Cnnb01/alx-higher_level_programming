#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    union_set = set_1 | set_2
    for i in set_1:
        if i in set_2:
            union_set.remove(i)
    return (union_set)
