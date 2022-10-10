#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    if my_list != 0:
        i = 0
        while i < x:
            try:
                print("{}".format(my_list[i]), end="")
            except IndexError:
                pass
            i += 1
            print("")
            return i
