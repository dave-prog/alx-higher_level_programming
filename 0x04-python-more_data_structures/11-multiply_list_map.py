#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    if my_list != 0:
        nw_list = my_list.copy()
        for i in range(len(nw_list)):
            nw_list[i] *= number
        return nw_list
