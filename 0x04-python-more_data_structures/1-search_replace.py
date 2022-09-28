#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if my_list != 0:
        nw_list = my_list.copy()
        for i in range(len(nw_list)):
            if nw_list[i] == search:
                nw_list[i] = replace
        return nw_list
