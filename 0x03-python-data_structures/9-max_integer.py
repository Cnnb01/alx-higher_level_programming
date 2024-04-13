#!/usr/bin/python3
def max_integer(my_list=[]):
    for nums in my_list:
        if not isinstance(nums, int):
            raise TypeError("List must contain only integers")
    max_num = my_list[0]
    if my_list == []:
        return (None)
    else:
        for i in range(len(my_list)):
            if my_list[i] > max_num:
                max_num = my_list[i]
        return (max_num)
