#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    arg = sys.argv
    args = arg[1:]
    n = len(args)

    if n == 0:
        print("{} arguments.".format(n))
    else:
        if n == 1:
            print("{} argument:".format(n))
        else:
            print("{} arguments:".format(n))
        for i in range(1, n+1):
            print("{}: {}".format(i, arg[i]))
