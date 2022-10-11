#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        return fct(*args)
    except (ZeroDivisionError, IndentationError, ValueError, TypeError, IndexError) as e:
        sys.stderr.write("Exception: {}".format(e))
        return None
