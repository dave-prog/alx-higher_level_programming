#!/usr/bin/python3

def uniq_add(my_list=[]):
    if my_list != 0:
        my_set = set(my_list)
        counter = 0
        for i in my_set:
            counter += i
        return counter
