#!/usr/bin/python3
def search_replace(my_list, search, replace):
    replacement = []
    for i in my_list:
        if i == search:
            i = replace
        replacement.append(i)
    return (replacement)
