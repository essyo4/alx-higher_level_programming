#!/usr/bin/python3
# 2-uniq_add.py


def uniq_add(my_list=[]):
    result = 0
    for x in set(my_list):
        result += x
    return (result)

# return (sum(set(my_list)))
