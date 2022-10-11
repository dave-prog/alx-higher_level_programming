#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    i = 0
    result = 0
    while i < x:
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                result += 1
        except (IndexError, TypeError, ValueError):
            break
        i += 1
    print("")
    return result
