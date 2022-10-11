#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        c = None
        return None
    finally:
        print("Inside result: {}".format(c))
